window.fakeStorage = {
  _data: {},

  setItem: function (id, val) {
    return this._data[id] = val;
  },

  getItem: function (id) {
    return this._data.hasOwnProperty(id) ? this._data[id] : undefined;
  },

  removeItem: function (id) {
    return delete this._data[id];
  },

  getItems: function () {
    return this._data;
  },

  clear: function () {
    return this._data = {};
  }
};

function LocalStorageManager() {
  this.gameState = undefined;
  this.storage = window.fakeStorage;
}

// Best score getters/setters
LocalStorageManager.prototype.getBestScore = function (userId) {
  var item = this.storage.getItem(userId);
  return item ? item.score : 0;
};

LocalStorageManager.prototype.setBestScore = function (userId, userName, score) {
  this.storage.setItem(userId, {"name": userName, "score": score});
};

LocalStorageManager.prototype.getScoreboard = function () {
  var dict = this.storage.getItems();
  var items = Object.keys(dict).map(function (key) {
    return [key, dict[key]["name"], dict[key]["score"]];
  });
  items.sort(function (first, second) {
    return second[2] - first[2];
  });
  return items;
};

// Game state getters/setters and clearing
LocalStorageManager.prototype.getGameState = function () {
  return this.gameState;
};

LocalStorageManager.prototype.setGameState = function (gameState) {
  this.gameState = gameState;
};

LocalStorageManager.prototype.clearGameState = function () {
  this.gameState = undefined;
};
