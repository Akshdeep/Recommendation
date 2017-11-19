console.log("Hello")
var xmlhttp = new XMLHttpRequest();
xmlhttp.onreadystatechange = function() {
  if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
    var data = JSON.parse(xmlhttp.response);
    show_results(data);
  } else if (xmlhttp.readyState == 4) {
    console.log('Something went wrong: ' + xmlhttp.status);
  }
}

xmlhttp.open('POST', 'http://127.0.0.1:5000/getdata', true);
xmlhttp.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');

function show_results(data) {
    console.log("hello")
    console.log(data)
    var div;
    var col;
    console.log(data);
    for (i = 0; i < 4; i++) {
        div = document.createElement('div');

        div.className = 'row';

        col = "";
        while (i % 3 !== 0 || i < data.length ) {
        col = col +'                <!--First column-->'+
        '                <div class="col-lg-4 wow fadeIn" data-wow-delay="0.2s">'+
        ''+
        '                    <!--Card-->'+
        '                    <div class="card">'+
        ''+
        '                        <!--Card image-->'+
        '                        <img class="img-fluid" src="http://image.tmdb.org/t/p/w300/' + data[i].poster_path +'" alt="Card image cap">'+
        ''+
        '                        <!--Card content-->'+
        '                        <div class="card-body">'+
        '                            <!--Title-->'+
        '                            <h4 class="card-title">'+data[i].name+'</h4>'+
        '                            <!--Text-->'+
        '                            <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card\'s content.</p>'+
        '                            <a href="#" class="btn btn-primary">Button</a>'+
        '                        </div>'+
        ''+
        '                    </div>'+
        '                    <!--/.Card-->'+
        ''+
        '                </div>'+
        '                <!--/.First column-->'
        i++;
        }
    div.innerHTML =  '<!--First row-->'+
    '            <div class="row mt-5 wow">'+
    col +
    '            </div>'+
    '            <!--/.First row-->';

    document.getElementById('maincontent').appendChild(div);
    }
}