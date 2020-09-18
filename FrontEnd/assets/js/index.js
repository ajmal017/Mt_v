

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

});