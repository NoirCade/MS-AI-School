$(window).on('scroll', function(e){
    let $ul = $('ul')
    let scrollNow = $(window).scrollTop();
    let menuNow = $ul.offset().top
    console.log(scrollNow, menuNow)

    if (scrollNow >= menuNow - 10) {
        $ul.css('position: fixed;', 'top: ' + menuNow - 10)
    } else {
        $ul.css('position: relative;')
    }
})
