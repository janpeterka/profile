var videoContainer = document.getElementById("video");
var videoPlayer = document.getElementById("videoPlayer");
var menu = document.getElementById("menu");
var menuOptions = document.getElementById("options");
var optionList = document.getElementById("optionList");

var json_source = `{
	"menus":
	[{
		"1": {
			"code_from": "1",
				"options": [{
					"first": {
						"label": "Go left",
						"code": "2a"
					},
					"second": {
						"label": "Go right",
						"code": "2b"
					}
				}]
		},
		
		"2": {
			"code_from": "2",
				"options": [{
					"first": {
						"label": "Turn around",
						"code": "3a"
					},
					"second": {
						"label": "Go right",
						"code": "4"
					}
				}]
		},

		"4": {
			"code_from": "4",
				"options": [{
					"first": {
						"label": "Go",
						"code": "5a"
					},
					"second": {
						"label": "Run!",
						"code": "5b"
					}
				}]
		}


	}]

}
`

json = JSON.parse(json_source);

function start_game(){
	playVideo()
	get_menu_options();
}

function get_menu_options() {
	var currentId = menu.dataset.currentId;
	set_menu_options(currentId);
}

function set_menu_options(id){
	
	options = json.menus[id].options;
	$(optionList).empty();

	for (var i = options.length - 1; i >= 0; i--) {
		$("<li><a id='"+options[i].code+"'>"+options[i].label+"</li>").appendTo(optionList);

	}
}

function playVideo() {
    // video.preload = "auto";
    videoPlayer.load();
    videoPlayer.play();
    // return video;
}

