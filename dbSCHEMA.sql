DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Exercise;
DROP TABLE IF EXISTS UserLifts;
PRAGMA foreign_keys = 1;

--CREATE TABLE weaponsP(wp_id PRIMARY KEY, wp_name, wp_class, wp_DamageTypes, wp_fireRate, wp_fireType, wp_noise);
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
	username TEXT,
	password TEXT,
    userExercises TEXT);

CREATE TABLE IF NOT EXISTS exercise(
    e_id INTEGER PRIMARY KEY,
    e_name TEXT,
    e_category TEXT, 
    e_muscleGroups TEXT 
);

CREATE TABLE IF NOT EXISTS userLifts(
    ul_exerciseID INTEGER,
    FOREIGN KEY(ul_exerciseID) REFERENCES exercise(e_id),
    ul_name TEXT,
    ul_musclegroup TEXT,
    ul_date DATE
 );

--cur.execute("INSERT INTO users (username, password, profile_id) VALUES (?, ?, ?)", ('bofa', 'deez', 69))

INSERT INTO users(username, password) VALUES(?, ?), ('bofa', 'deez');
INSERT INTO users(username, password) VALUES(?, ?), ('1', 'deez');