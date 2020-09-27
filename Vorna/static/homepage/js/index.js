

$(document).ready(function () {
//     $(".menuIconBordered").click(function () {
//         $(".menuIconBordered").toggleClass("menuIconBordered_clicked")
//     });

    // $('.menuIconBordered').on('click', function () {
    //     $('#sidebar-main ').toggleClass('active');
    // });

    // $('#clock-icon').on('click', function () {
    //     $('#sidebar-clock ').toggleClass('active');
    //     $('#clock-icon').toggleClass("iconClicked")
    // });

    // $('#menu-icon').on('click', function () {
    //     $('.body-scrollable').toggleClass('body-scrollable-callaps');
    //     $('#sidebar-main ').toggleClass('active');
    //     // $('#sidebar-main ').toggleClass('col-md-3');
    //     $('#menu-icon').toggleClass("iconClicked");
    // });

    // $('.menuIconBordered').toggle(
    //     function(){
    //         $(this).css('background-color', 'blue');
    //     },
    //     function(){
    //         $(this).css('background-color', 'red');
    //     });
    var d=new Date();
    var time=d.toLocaleTimeString();
    var date=d.toLocaleDateString();
    setInterval(function(){
        d=new Date();
        date=d.toLocaleDateString();
        time=d.toLocaleTimeString();
        $("#time").html(time);
        $("#date").html(date);
    }, 1000);
    /////////////////////////////////adding css to table///////////////////////////////
    $(".myTable tr td:first-child").html("<div class='green larg'>1.56</div>" +
        "<div class='red short'>1235</div>");
    $(".myTable tr td:nth-child(2)").html("1235");
    $("#shakhes-keshvarha tr td:first-child").html("<div class='green '>9:00:00</div>" +
        "<div class='red '>22:00:00</div>");
    $("#shakhes-keshvarha tr td:nth-child(2)").html("<div class='green larg'>1.56</div>" +
        "<div class='red short'>1235</div>");
    ///////////////////////////////////////////darkmod-func////////////////////////////
    var darkMode=false;
    $("#darkmode-icon").on("click",function() {
        darkMode = !darkMode;
        var theme = "light"
        if (darkMode == true) {
            theme = "dark";
        } else {
            theme = "light";
        }
        $(".body-scrollable").toggleClass("body-scrollable-dark");
        $(".table-container").toggleClass("table-container-dark");
        $(".myCard").toggleClass("myCard-dark");
        $(".myTable").toggleClass("myTable-dark");
        $(".table-hover ").toggleClass("table-hover-dark");
        $(".owl-carousel ").toggleClass("owl-carousel-dark");
        $(".news-header ").toggleClass("news-header-dark");
        $(".news-title ").toggleClass("news-title-dark");
        $(".owl-prev").toggleClass("owl-prev-dark");
        $(".owl-next").toggleClass("owl-next-dark");
        $(".sideBar").toggleClass("sideBar-dark");
        if (darkMode) {
            $("#tradingview-widget-container").html("" +
                "                    <div class=\"tradingview-widget-container\">\n" +
                "                        <div id=\"tradingview_7bf78\"></div>\n" +
                "                        <div class=\"tradingview-widget-copyright\"><a href=\"https://www.tradingview.com/symbols/NASDAQ-AAPL/\" rel=\"noopener\" target=\"_blank\"><span class=\"blue-text\">AAPL Chart</span></a> by TradingView</div>\n" +
                "                        <script type=\"text/javascript\" src=\"https://s3.tradingview.com/tv.js\"></script>\n" +
                "                        <div id=\"chart\">\n" +
                "                            <script type=\"text/javascript\">\n" +
                "                                // var theme=\"dark\";\n" +
                "                                var tw=new TradingView.widget(\n" +
                "                                    {\n" +
                "                                        \"autosize\": true,\n" +
                "                                        \"symbol\": \"NASDAQ:AAPL\",\n" +
                "                                        \"interval\": \"D\",\n" +
                "                                        \"timezone\": \"Etc/UTC\",\n" +
                "                                        \"theme\": \"dark\",\n" +
                "                                        \"style\": \"1\",\n" +
                "                                        \"locale\": \"en\",\n" +
                "                                        \"toolbar_bg\": \"#f1f3f6\",\n" +
                "                                        \"enable_publishing\": false,\n" +
                "                                        \"withdateranges\": true,\n" +
                "                                        \"hide_side_toolbar\": false,\n" +
                "                                        \"allow_symbol_change\": true,\n" +
                "                                        \"watchlist\": [\n" +
                "                                            \"BTC\"\n" +
                "                                        ],\n" +
                "                                        \"details\": true,\n" +
                "                                        \"hotlist\": true,\n" +
                "                                        \"calendar\": true,\n" +
                "                                        \"show_popup_button\": true,\n" +
                "                                        \"popup_width\": \"1000\",\n" +
                "                                        \"popup_height\": \"650\",\n" +
                "                                        \"container_id\": \"tradingview_7bf78\"\n" +
                "                                    }\n" +
                "                                );\n" +
                "                            </script>\n" +
                "                        </div>\n" +
                "                    </div>\n ");
        } else {
            $("#tradingview-widget-container").html("" +
                "                    <div class=\"tradingview-widget-container\">\n" +
                "                        <div id=\"tradingview_7bf78\"></div>\n" +
                "                        <div class=\"tradingview-widget-copyright\"><a href=\"https://www.tradingview.com/symbols/NASDAQ-AAPL/\" rel=\"noopener\" target=\"_blank\"><span class=\"blue-text\">AAPL Chart</span></a> by TradingView</div>\n" +
                "                        <script type=\"text/javascript\" src=\"https://s3.tradingview.com/tv.js\"></script>\n" +
                "                        <div id=\"chart\">\n" +
                "                            <script type=\"text/javascript\">\n" +
                "                                // var theme=\"dark\";\n" +
                "                                var tw=new TradingView.widget(\n" +
                "                                    {\n" +
                "                                        \"autosize\": true,\n" +
                "                                        \"symbol\": \"NASDAQ:AAPL\",\n" +
                "                                        \"interval\": \"D\",\n" +
                "                                        \"timezone\": \"Etc/UTC\",\n" +
                "                                        \"theme\": \"light\",\n" +
                "                                        \"style\": \"1\",\n" +
                "                                        \"locale\": \"en\",\n" +
                "                                        \"toolbar_bg\": \"#f1f3f6\",\n" +
                "                                        \"enable_publishing\": false,\n" +
                "                                        \"withdateranges\": true,\n" +
                "                                        \"hide_side_toolbar\": false,\n" +
                "                                        \"allow_symbol_change\": true,\n" +
                "                                        \"watchlist\": [\n" +
                "                                            \"BTC\"\n" +
                "                                        ],\n" +
                "                                        \"details\": true,\n" +
                "                                        \"hotlist\": true,\n" +
                "                                        \"calendar\": true,\n" +
                "                                        \"show_popup_button\": true,\n" +
                "                                        \"popup_width\": \"1000\",\n" +
                "                                        \"popup_height\": \"650\",\n" +
                "                                        \"container_id\": \"tradingview_7bf78\"\n" +
                "                                    }\n" +
                "                                );\n" +
                "                            </script>\n" +
                "                        </div>\n" +
                "                    </div>\n ");
        }

    });
});
/*******************************************************************news slider***********/
$(".flickity-slider").css("transform","translateX(0)");
// transform: translateX(32.36%);
window.addEventListener('load', function(){
    new Glider(document.querySelector('.glider'), {
        slidesToScroll: 1,
        slidesToShow: 3,
        draggable: true,
        dots: '.dots',
        // scrollLock:true,
        // scrollLockDelay:550,
        rewind:true,
        dragVelocity:1,
        duration:1.5,
        arrows: {
            prev: '.glider-prev',
            next: '.glider-next'
        }
    });
});

$('.owl-carousel').owlCarousel({
    animateOut: 'slideOutDown',
    animateIn: 'flipInX',
    touchDrag:true,
    pullDrag:true,
    loop:true,
    nav:true,
    margin:4,
    responsiveClass:true,
    responsive:{
        0:{
            items:1,
            nav:true
        },
        700:{
            items:2,
            nav:true
        },
        900:{
            items:3,
            nav:true
        },

    }
});
owl.on('mousewheel', '.owl-stage', function (e) {
    if (e.deltaY>0) {
        owl.trigger('next.owl');
    } else {
        owl.trigger('prev.owl');
    }
    e.preventDefault();
});
