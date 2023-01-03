console.log ("main_js");
document.getElementById('stakan').addEventListener('click', onstakan);

function onstakan(event) {
    console.log ("onstakan");
    let target = event.target; // где был клик?
    let imyaid = target.attributes[1].value;     //  attribute, например b2
    let currcell = document.querySelector('#'+imyaid);
    let my_href = document.querySelector('#my_href');
    my_param = currcell.innerHTML.trim();
    my_href.setAttribute('href', "/show_mesto/"+my_param);

    console.log('imyaid = ');
    console.log(imyaid);
    console.log(currcell.innerHTML);
    let cell_name = document.querySelector('#for_href');
    cell_name.innerHTML = currcell.innerHTML;

    /*
    fetch('http://localhost:9000/before_show_mesto/'+currcell.innerHTML)
      .then(data => console.log(data));
    */

};


