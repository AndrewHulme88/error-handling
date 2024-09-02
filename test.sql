CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO users (username, password_hash) VALUES
('my_name', 'my_super_secret_password');

SELECT user_id, username
FROM users
WHERE username = 'my_name' AND password_hash = 'my_super_secret_password';
