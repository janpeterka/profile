/* TODO
 - jiné rozlišení
*/
var container = document.getElementById("container");
var videoContainer = document.getElementById("video");
var videoPlayer = document.getElementById("videoPlayer");
videoPlayer.addEventListener('ended', handler_video_end, false);
var videoSource = document.getElementById("videoSource");
container.addEventListener('click', set_full_screen, false);

var menu = document.getElementById("menu");
var optionsLabel = document.getElementById("optionsLabel");
var menuOptions = document.getElementById("options");
var optionList = document.getElementById("optionList");

var lastVideoCode = "8";

var json_source = `{
	"menus":
	{
		"0": {
			"label": "This Game",
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

		"2": {},
		
		"3": {
			"label": "What do you do?",
			"options": [
				{
					"label": "Turn around and go right",
					"code": "4a"
				},
				{
					"label": "Go right",
					"code": "4b"
				}
			]
		},

		"4": {
			"label": "How do you continue?",
			"options": [
				{
					"label": "Go",
					"code": "5b"
				},
				{
					"label": "Run!",
					"code": "5a"
				}
			]
		},

		"5": {},

		"6": {
			"label": "You see a door to the building.",
			"options": [
				{
					"label": "Run",
					"code": "7a"
				},
				{
					"label": "Hide in the building",
					"code": "7b"
				}
			]
		},

		"7": {},

		"8": {
			"label": "You are tired.",
			"options": [
				{
					"label": "Give up",
					"code": "9a"
				},
				{
					"label": "Run to the tunnel!",
					"code": "9b"
				}
			],
			"next": {
				"9a":
					{
						"next": "game_over"
					},
				"9b":
					{
						"next": "end_of_level"
					}
			}
		},

		"game_over": {
			"label": "Game over"
		} ,

		"end_of_level": {
			"label": "End of level"
		}


	}

}
`


json = JSON.parse(json_source);

function set_full_screen(){
	container.requestFullscreen();
}

function prepare_game(){
	set_menu_options(lastVideoCode);
	// container.requestFullscreen();
}

function select_option(code){
	playVideo(code);
}

function set_current_video_id(){
	// get number from code (or number)
	if (typeof(lastVideoCode) == "number"){
		currentVideoId = lastVideoCode;
	} else {
		currentVideoId = lastVideoCode.match(/\d+/g)[0];
	}
}

function get_menu_options() {
	if (json["menus"][currentVideoId].hasOwnProperty("options")){
		set_menu_options(currentVideoId);
	} else {
		playVideo(parseInt(currentVideoId) + 1);
	}
}

function set_menu_options(id){
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

	menu.classList.remove("hidden")
}

function set_screen(situation){
	$(optionsLabel).empty();
	optionsLabel.innerHTML = "<h3>"+situation["label"]+"<h3>"
	$(optionList).empty();
	menu.classList.remove("hidden")
}

function show_endscreen(){
	next_code = json["menus"][currentVideoId - 1]["next"][lastVideoCode]["next"]
	next = json["menus"][next_code]
	set_screen(next)
}

function setVideo(code) {
	videoSource.setAttribute('src', "static/videos/"+code+".webm");
    lastVideoCode = code
}

function playVideo(code) {
	setVideo(code);
    video.preload = "auto";
    videoPlayer.load();

    videoContainer.classList.remove("blurred");
    menu.classList.add("hidden");

    videoPlayer.play();
}

function handler_video_end(e) {
	set_current_video_id();
    videoContainer.classList.add("blurred");
    if (currentVideoId != 9){
		get_menu_options();
    } else {
    	show_endscreen();
    }
}


window.onload = prepare_game()