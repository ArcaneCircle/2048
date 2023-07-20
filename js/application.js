import "webxdc-scores";
import { GameManager } from "./game_manager.js";
import { KeyboardInputManager } from "./keyboard_input_manager.js";
import { HTMLActuator } from "./html_actuator.js";

// Wait till the browser is ready to render the game (avoids glitches)
window.requestAnimationFrame(function () {
  window.highscores.init("2048", "scoreboard").then(() => {
    const gameManager = new GameManager(4, KeyboardInputManager, HTMLActuator);
    document.addEventListener("visibilitychange", () => {
      window.highscores.setScore(gameManager.score);
    });
  });
});
