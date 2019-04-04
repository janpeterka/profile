// Global use variables


var difficulty = 0;
// Card count
var size = 0;

// face-up timeout
var tout = 600;
// game started
var game = false;
// player's turn
var turn = true;

// moves system variables
var time = 0;
var moves = 0;
var score = 0;
var npc_score = 0;
var logbook = "";

var diff_div = document.getElementById("diff_show");
var timer_div = document.getElementById("timer");
var score_div = document.getElementById("score");
var npc_score_div = document.getElementById("npc_score");
var moves_div = document.getElementById("moves");

var timer_full = document.getElementById("timer_full");
var score_full = document.getElementById("score_full");
var npc_score_full = document.getElementById("npc_score_full");
var moves_full = document.getElementById("moves_full");

var guess1 = "";
var guess2 = "";
var count = 0;


// Time interval
setInterval(function() {
    var minute_text;
    var second_text;
    var seconds;
    var minutes;
    if (game === true) {
        time += 1;
        minutes = Math.floor(time / 60);
        seconds = time % 60;
        if (minutes != 1) {
            minute_text = "minutes";
        } else {
            minute_text = "minute";
        }
        if (seconds != 1) {
            second_text = "seconds";
        } else {
            second_text = "second";
        }


        if (minutes < 1) {
            timer_full.innerHTML = seconds + " " + second_text;
        } else if (seconds === 0) {
            timer_full.innerHTML = minutes + " " + minute_text;
        } else {
            timer_full.innerHTML = minutes + " " + minute_text + " and " + seconds + " " + second_text;
        }

    }
}, 1000);

Array.prototype.randomize = function() {
    var currentIndex = this.length,
        temporaryValue, randomIndex;

    // While there remain elements to shuffle...
    while (0 !== currentIndex) {

        // Pick a remaining element...
        randomIndex = Math.floor(Math.random() * currentIndex);
        currentIndex -= 1;

        // And swap it with the current element.
        temporaryValue = this[currentIndex];
        this[currentIndex] = this[randomIndex];
        this[randomIndex] = temporaryValue;
    }

    return this;
};

// get images, place them in an array & randomize the order
function makeCards(size) {
    var images = [];

    for (let i = 1; i < (parseInt(size) + 1); i++) {
        var img = 'templates/pics/' + i + '.jpg';
        // var path = 'pics/' + i + '.jpg';
        // var img = "{{ url_for('static', filename='" + path + "') }}"
        console.log("img");
        console.log(img);

        images.push(img);
        images.push(img);
    }
    images.randomize();

    // output images then hide them
    var output = "<ol>";

    for (let i = 0; i < (size + 1) * 2 - 2; i++) {
        output += '<li id="img' + i + '">';
        output += "<img src = '" + images[i] + "'/>";
        console.log(output)
        output += "</li>";
    }
    output += "</ol>";
    document.getElementById("container").innerHTML = output;
}


// Set all values to default before user is allowed to play
restart();


// Use on <li>
$.fn.playCard = function playCard() {
    if ((count < 2) && ($(this).children("img").hasClass("face-up")) === false) {

        // Start a game, if first move
        if (game === false) {
            game = true;
        }
        // Check, if valid - only one card turned
        if (count >= 2) {
            count = 0;
            return;
        }

        if (turn === true) {
            moves += 1;
            moves_div.innerHTML = Math.floor(moves / 2);
        }



        // increment guess count, show image, mark it as face up
        count++;
        $(this).children("img").show();
        $(this).children("img").addClass("face-up");
        $(this).children("img").addClass("temp_memory");


        //guess #1
        if (count == 1) {
            guess1 = $(this).children("img").attr("src");
        }

        //guess #2
        else if (count == 2) {
            guess2 = $(this).children("img").attr("src");


            // since it's the 2nd guess check for match
            if (guess1 == guess2) {
                console.log("match");
                $("li").children("img[src='" + guess1 + "']").addClass("match");
                $("li").children("img[src='" + guess1 + "']").removeClass("temp_memory,,,,");

                $(this).children("img").removeClass("memory");
                if (turn === true) {
                    score += 1;
                    score_div.innerHTML = score;
                } else {
                    npc_score += 1;
                    npc_score_div.innerHTML = npc_score;
                }


                if (score + npc_score == size) {
                    turn = true;
                    setTimeout(function() {
                        endGame();
                    }, 100);
                }

                setTimeout(function() {
                    if (count == 2) {
                        count = 0;
                    }
                }, tout);


            }

            // else it's a miss
            else {
                console.log("miss");
                // if not singleplayer
                if (difficulty !== 0) {
                    turn = !turn;
                }
                console.log(turn);

                setTimeout(function() {
                    $("img").not(".match").removeClass("face-up");
                    if (count == 2) {
                        count = 0;
                    }
                }, tout);
            }

            if (turn === false) {
                setTimeout(function() {
                    console.log("will play");
                    npcTurn();
                }, 2000);
            }
            $("li").children("img.temp_memory").addClass("memory");
            $("li").children("img.temp_memory").removeClass("temp_memory");
        }

    }
};



function restart() {
    time = 0;
    moves = 0;
    score = 0;
    npc_score = 0;
    game = false;
    turn = true;

    moves_div.innerHTML = moves;
    timer_full.innerHTML = "0 seconds";
    score_div.innerHTML = score;
    npc_score_div.innerHTML = npc_score;


    $("img").removeClass("face-up");
    $("img").removeClass("match");
    $("img").removeClass("memory");
    $("img").removeClass("temp_memory");

    size = parseInt($("#size").val());

    makeCards(size);

    difficulty = parseInt($("#difficulty").val());
    diffs = ["Singleplayer", "Beginner", "Easy", "Advanced", "Expert", "Nightmare"];
    diff_div.innerHTML = diffs[difficulty];

    if (difficulty === 0) {
        npc_score_full.style.display = "none";
    } else {
        npc_score_full.style.display = "block";
    }



    // Makes <li> clickable
    $("li").click(function() {
        if (turn === true) {
            $(this).playCard();
        }
    });

    console.log("Game restarted.");


}

function endGame() {
    game = false;
    if (score > npc_score) {
        alert("You have won!\nScore " + score + " : " + npc_score);

    } else if (score == npc_score) {
        alert("It was a tie.\nScore " + score + " : " + npc_score);
    } else {
        alert("You have lost!\nScore " + score + " : " + npc_score);
    }
    restart();

}

function npcTurn() {
    var ok;

    if (difficulty === 0) {
        console.log("not played");
        turn = true;

    } else if (difficulty == 1) {
        $("li").children("img").not(".face-up").random().parent().playCard();
        $("li").children("img").not(".face-up").random().parent().playCard();

    } else if (difficulty == 2) {
        semirandMove();
    } else if (difficulty == 3) {
        for (var i = $("li").children("img.memory").length - 1; i >= 0; i--) {
            for (var j = $("li").children("img.memory").length - 1; j >= 0; j--) {
                if (i != j) {
                    if ($("li").children("img.memory").eq(i).attr("src") == $("li").children("img.memory").eq(j).attr("src")) {
                        $("li").children("img.memory").eq(i).parent().playCard();
                        $("li").children("img.memory").eq(j).parent().playCard();
                        console.log("played same");
                        return;
                    }
                }
            }
        }
        semirandMove();
    } else {
        console.log("Something is wrong.");
    }

    console.log("npc out");
}

$.fn.random = function random() {
    rand = Math.floor(Math.random() * this.length);
    return this.eq(rand);
};

// NPC moves
function semirandMove() {
    var ok;
    var chosen = $("li").children("img").not(".face-up").random();
    chosen.parent().playCard();
    chosen.removeClass("memory");

    for (var i = $("li").children("img.memory").length - 1; i >= 0; i--) {
        if (chosen.attr("src") == $("li").children("img.memory").eq(i).attr("src")) {
            $("li").children("img.memory").eq(i).parent().playCard();
            ok = 1;

            break;
        }
    }
    if (ok != 1) {
        chosen.addClass("memory");
        $("li").children("img").not(".face-up").random().parent().playCard();
    }
}