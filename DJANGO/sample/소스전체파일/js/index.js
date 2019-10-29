// window.addEventListener('load, function() {
//   var menuopen = false;
//   var menuBtn = document.querySelector('.global-menu-btn');
//
//   menuBtn.addEventListener('click', function() {
//     var bodyElem = document.querySelector('body');
//
//     if(menuopen){
//       bodyElem.classList.remove('menu-on');
//       menuopen = false;
//     } else {
//       bodyElem.classList.add('menu-on');
//       menuopen = true;
//     }
//   });
// });

(function() {

    var menuBtn = document.querySelector('.global-menu-btn');

    menuBtn.addEventListener('click', function() {
        document.body.classList.toggle('menu-on');
    });

})();
