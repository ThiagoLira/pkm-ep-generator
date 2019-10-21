function displayLoader(loaderObj,display){
  var i;
  for (i = 0; i < loaderObj.length; i++) {
    loaderObj[i].style.display = display;
  }

}


function callGeneratorAjax(){



    // user prefix text
    var textbox = document.getElementById("text")

    var prefix  = document.getElementById("prefix_text").value

    var loaders = document.getElementsByClassName("lds-grid")


    displayLoader(loaders,"inline-block")
    $.ajax({
        method: 'GET',
        url: 'http://ec2-18-228-30-26.sa-east-1.compute.amazonaws.com/?sample=' + prefix,
        // url: 'http://localhost:5000/?sample=' + prefix,  
        dataType: 'jsonp', //change the datatype to 'jsonp' works in most cases
        success: (res) => {

            textbox.textContent = res.sample_text;
            displayLoader(loaders,"None")
        }
    })

}



function callGeneratorMock(){



    // user prefix text
    var textbox = document.getElementById("text")

    var prefix  = document.getElementById("prefix_text").value

    var loaders = document.getElementsByClassName("lds-grid")

    console.log("hello")

    displayLoader(loaders,"inline-block")
    $.ajax({
        method: 'GET',
        url: 'http://localhost:5000/mock',  
        dataType: 'json', //change the datatype to 'jsonp' works in most cases
        success: (res) => {
            textbox.textContent = res.sample_text;
            displayLoader(loaders,"None")
        }
    })

}


function callGenerator(){
  // user prefix text
    var textbox = document.getElementById("text")

    var prefix  = document.getElementById("prefix_text").value

    var loaders = document.getElementsByClassName("lds-grid")

    var xmlHttp = new XMLHttpRequest();
      xmlHttp.onreadystatechange = function() {
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200){
            textbox.textContent = JSON.parse(xmlHttp.responseText).sample_text;
            displayLoader(loaders,"None")
        }
       else{
           // displayLoader(loaders,"None")
            }
      }


    displayLoader(loaders,"inline-block")
    var url = "http://localhost:5000/?sample=" + prefix
    xmlHttp.open( "GET", url, true );
    xmlHttp.send( null );
}





