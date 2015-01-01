var margin = {top: 50, right: 50, bottom: 100, left: 100},
width = window.innerWidth - margin.left - margin.right -50,
height = window.innerHeight - margin.top - margin.bottom -50;

var parseDate = d3.time.format("%Y-%m-%d %H:%M:%S").parse;

var x = d3.time.scale()
    .range([0, width]);

var yByte = d3.scale.pow()
    .exponent(0.5)
    .range([height, 0]);

var yLease = d3.scale.linear()
    .range([height, 0]);

var xAxis = d3.svg.axis()
    .scale(x)
    .orient("bottom");

var yByteAxis = d3.svg.axis()
    .scale(yByte)
    .orient("left");

var yLeaseAxis = d3.svg.axis()
    .scale(yLease)
    .orient("right");

var Byteline = d3.svg.area()
    .interpolate("basis")
    .x(function(d) { return x(d.date); })
    .y(function(d) { return yByte(d["RX"]); });

var Leaseline = d3.svg.line()
    .x(function(d) { return x(d.date); })
    .y(function(d) { return yLease(d["lease"]); });

var area = d3.svg.area()
    .interpolate("basis")
    .x(function(d) { return x(d.date); })
    .y1(function(d) { return yByte(d["RX"]); });

var svg = d3.select("#content").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

d3.tsv("http://devlol.org/devmon/data/day.tsv", function(error, data) {
    data.forEach(function(d) {
        d.date = parseDate(d.date);
        d["RX"]= +d["RX"];
        d["TX"] = +d["TX"];
        d["lease"] = +d["lease"];
    });

    x.domain(d3.extent(data, function(d) { return d.date; }));

    yByte.domain([
        d3.min(data, function(d) { return Math.min(d["RX"], d["TX"]); }),
            d3.max(data, function(d) { return Math.max(d["RX"], d["TX"]); })
            ]);

    yLease.domain([
        d3.min(data, function(d) { return Math.min(d["lease"]); }),
            d3.max(data, function(d) { return Math.max(d["lease"]); })
            ]);

    svg.datum(data);

    svg.append("clipPath")
        .attr("id", "clip-below")
        .append("path")
        .attr("d", area.y0(height));

    svg.append("clipPath")
        .attr("id", "clip-above")
        .append("path")
        .attr("d", area.y0(0));

    svg.append("path")
        .attr("class", "area above")
        .attr("clip-path", "url(#clip-above)")
            .attr("d", area.y0(function(d) { return yByte(d["TX"]); }));

    svg.append("path")
        .attr("class", "area below")
        .attr("clip-path", "url(#clip-below)")
            .attr("d", area);

    svg.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(0," + height + ")")
        .call(xAxis);

    svg.append("g")
        .attr("class", "y axis")
        .call(yByteAxis)
        .append("text")
        .attr("transform", "rotate(-90)")
        .attr("y", 6)
        .attr("dy", ".71em")
        .style("text-anchor", "end")
        .text("KB/s");

    svg.append("g")             
        .attr("class", "y axis")    
        .attr("transform", "translate(" + width + " ,0)")   
        .call(yLeaseAxis)
        .append("text")
        .attr("transform", "rotate(-90)")
        .attr("y", -12)
        .attr("dy", ".71em")
        .style("text-anchor", "end")
        .text("DHCP-Leases");


    svg.append("path")
        .attr("class", "Byteline")
        .attr("d", Byteline);

    svg.append("path")
        .attr("class", "Leaseline")
        .attr("d", Leaseline);
});
