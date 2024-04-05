document.querySelector('#bnt-menu-nav').addEventListener('click', function() {
    // const 
    const menu = document.querySelector('.menu-close');
    const animButonMenu = document.querySelector('.bnt-menu-nav-close');
    menu.classList.toggle('menu-open');
    animButonMenu.classList.toggle('bnt-menu-nav-open');

  });

  document.querySelectorAll('.click-btn').forEach(item => {
    item.addEventListener('click', function(event) {
        const click = document.querySelector('.menu-open');
        const animButonMenu = document.querySelector('.bnt-menu-nav-close');

        if (click) {
            click.classList.remove('menu-open');
            animButonMenu.classList.remove('bnt-menu-nav-open');
        }
    });
});

const animateItem = document.querySelectorAll('.animate-item')
const animateContainer = document.querySelectorAll('.animate-container')

const myObseverItem = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        if (entry.isIntersecting) {
            entry.target.classList.add('animate-item-active')
        }else{
            entry.target.classList.remove('animate-item-active')
        }
    })
})

const myObseverContainer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        if (entry.isIntersecting) {
            entry.target.classList.add('animate-container-active')
        }else{
            entry.target.classList.remove('animate-container-active')
        }
    })
})

animateContainer.forEach(container => {
    myObseverContainer.observe(container)
})

animateItem.forEach(item => {
    myObseverItem.observe(item)
})
  