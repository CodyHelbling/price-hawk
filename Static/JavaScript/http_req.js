

function test(){
    console.log("PriceHawk: http_req.js loaded.");
}


var HttpClient = function() {
    this.get = function(aUrl, aCallback) {
        var anHttpRequest = new XMLHttpRequest();
        anHttpRequest.onreadystatechange = function() { 
            if (anHttpRequest.readyState == 4 && anHttpRequest.status == 200)
                aCallback(anHttpRequest.responseText);
        }

        anHttpRequest.open( "GET", aUrl, true );            
        anHttpRequest.send( null );
    }
}


test_url = 'https://www.amazon.com/Dell-210-ADRZ-DELL-UltraSharp-UP2715K/dp/B00R420SU4/ref=sr_1_9?s=pc&ie=UTF8&qid=1484685159&sr=1-9&keywords=monitor&refinements=p_n_feature_three_browse-bin%3A12659079011'

function add_url(){
    console.log('PriceHawk: http_req.js add_url()');

    var client = new HttpClient();
    url = document.getElementById("new_url");
    console.log(url);
    if(url != ''){
	client.get( window.location.origin +
		    "/add_url?name=Cody" +
		    "&url=" +
		    url,
		    function(response) {
			// do something with response
			console.log(response)
		    });
    }
    else{
	console.log("PriceHawk: No Url specified.");
    }
}
    
