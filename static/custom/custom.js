$(document).ready(function() {
    var limit = 4;
    var start = 0;
    var page = 1;
    var action = 'inactivate';
    function load_country_data(limit, start){
        $.ajax({
            type: "GET",
            url: "/loader/",
            data: {limit:limit, start:start, page:page },
            success: function (data) {
                $('#load_data').append(data);
                if(data == ''){
                    $('#load_data_message').html("<h4>No data </h4>");
                    action = 'activate'
                }
                else{
                    $('#load_data_message').html("<h4>please wait </h4>");
                    action = 'inactivate';
                }
            }

        });

    }

    if(action == 'inactivate'){
        action = 'activate';
        load_country_data(limit, start, page);

    }
    $(window).scroll(function(){

        if($(window).scrollTop() + $(window).height() > $("#load_data").height() && action == 'inactivate'){
            action = 'activate';
            start = start + limit;
            page = page + 1;
            setTimeout(function() {
                load_country_data(limit, start, page);
            },1000);

        }


    })

});


var infinite = new Waypoint.Infinite({
    element: $('.infinite-container')[0]
    onBeforePageLoad: function () {
        $('.loading').show();
    },
    onAfterPageLoad: function ($items) {
        $('.loading').hide();
    }


});