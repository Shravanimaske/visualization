
function fetchData(filters) {
    
    $.ajax({
        url: '/api/data/',
        type: 'GET',
        data: filters,
        success: function (data) {
            
            updateCharts(data);
        },
        error: function (error) {
            console.error('Error fetching data:', error);
        }
    });
}


function updateCharts(data) {
    
    d3.select('#chart1').html('');

    
    const svg = d3.select('#chart1')
        .append('svg')
        .attr('width', 400)
        .attr('height', 200);

    svg.selectAll('rect')
        .data(data)
        .enter()
        .append('rect')
        .attr('x', (d, i) => i * 50)
        .attr('y', (d) => 200 - d.intensity) 
        .attr('width', 40)
        .attr('height', (d) => d.intensity * 2)
        .attr('fill', 'blue');
}

$('#year-filter').change(function () {
    const selectedYear = $(this).val();
    const filters = {
        year: selectedYear
        
    };

   
    fetchData(filters);
});

const defaultFilters = {
    
};

fetchData(defaultFilters);
