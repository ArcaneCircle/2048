import "./scoreboard.css";
import "./main.css";

import "@webxdc/highscores";
import { GameManager } from "./game_manager.js";
import { KeyboardInputManager } from "./keyboard_input_manager.js";
import { HTMLActuator } from "./html_actuator.js";

const scoreboard = document.getElementById("scoreboard");
window.highscores
  .init({
    onHighscoresChanged: () => {
      scoreboard.innerHTML = window.highscores.renderScoreboard().innerHTML;
    },
  })
  .then(() => {
    // Wait till the browser is ready to render the game (avoids glitches)
    window.requestAnimationFrame(() => {
      const gameManager = new GameManager(
        4,
        KeyboardInputManager,
        HTMLActuator,
      );
      document.addEventListener("visibilitychange", () => {
        window.highscores.setScore(gameManager.score);
      });
    });
  });
