
const elementor = document.querySelector('.contacts-content')

const myObsever = new IntersectionObserver((entries) => {
    console.log(entries)
})

myObsever.observe(elementor)
console.log("Aparecendo por aqui")
console.log("Deu certo?");


document.querySelector('#bnt-menu-nav').addEventListener('click', function() {
    // const 
    const menu = document.querySelector('.menu-close');
    const animButonMenu = document.querySelector('.bnt-menu-nav-close');
    menu.classList.toggle('menu-open');
    animButonMenu.classList.toggle('bnt-menu-nav-open');

  });

  document.querySelectorAll('.click-btn').forEach(item => {
    item.addEventListener('click', function(click) {
        const click = document.querySelector('.menu-open');
        const animButonMenu = document.querySelector('.bnt-menu-nav-close');

        if (click) {
            click.classList.remove('menu-open');
            animButonMenu.classList.remove('bnt-menu-nav-open');
        }
    });
});

  