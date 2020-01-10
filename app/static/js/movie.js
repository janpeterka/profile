var videoContainer = document.getElementById("video");
var videoPlayer = document.getElementById("videoPlayer");
videoPlayer.addEventListener('ended', handler_video_end, false);
var videoSource = document.getElementById("videoSource");

var menu = document.getElementById("menu");
var optionsLabel = document.getElementById("optionsLabel");
var menuOptions = document.getElementById("options");
var optionList = document.getElementById("optionList");

var currentVideoCode = "0";

var json_source = `{
	"menus":
	{
		"0": {
			"label": "Game",
			"options": [
				{
					"label": "Start",
					"code": "1"
				}
			]

		},

		"1": {
			"label": "Where do you want to go?",
			"options": [
				{
					"label": "Go right",
					"code": "2a"
				},
				{
					"label": "Go left",
					"code": "2b"
				}
			]
		},
		
		"2": {
			"label": "What do you do?",
			"options": [
				{
					"label": "Turn around and go right",
					"code": "3a"
				},
				{
					"label": "Go right",
					"code": "3b"
				}
			]
		},

		"3": {
				"options": {
					"first": {
						"label": "Go",
						"code": "4a"
					},
					"second": {
						"label": "Run!",
						"code": "4b"
					}
				}
		}

	}

}
`
json = JSON.parse(json_source);

function prepare_game(){
	set_menu_options(currentVideoCode);
}

function select_option(code){
	console.log("selected: " + code);
	setVideo(code);
	playVideo();
}

function get_menu_options() {
	currentVideoId = currentVideoCode.match(/\d+/g)[0];
	set_menu_options(currentVideoId);
}

function set_menu_options(id){
	// console.log(id);
	situation = json["menus"][id]
	options = situation["options"];

	// Prepare situation label
	$(optionsLabel).empty();
	optionsLabel.innerHTML = "<h3>"+situation["label"]+"<h3>"


	// Prepare option list
	$(optionList).empty();

	for (var i = options.length - 1; i >= 0; i--) {
		$("<li><a onclick='select_option(\""+options[i]["code"]+"\")' id='"+options[i]["code"]+"'>"+options[i]["label"]+"</li>").appendTo(optionList);
	}

	menu.classList.remove("hide")
}

function setVideo(code) {
	videoSource.setAttribute('src', "static/videos/"+code+".webm");
    currentVideoCode = code
}

function playVideo() {

    // video.preload = "auto";
    videoPlayer.load();
    videoContainer.classList.remove("blurred");
    // videoContainer.classList.add("unblurred");
    menu.classList.add("hide");
    videoPlayer.play();
}

function handler_video_end(e) {
	get_menu_options();
    videoContainer.classList.add("blurred");
    // videoContainer.classList.remove("unblurred");
}





window.onload = prepare_game()