CREATE TABLE IF NOT EXISTS 'user' (
    'id' int(6) NOT NULL AUTO_INCREMENT,
    'email' varchar(255) NOT NULL,
    'fname' varchar(100) NOT NULL,
    'lname' varchar(100) NOT NULL,
    'password' varchar(255) NOT NULL,

    'admin' boolean NOT NULL,
    
    'created_at' timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    'updated_at' timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY ('id')
)