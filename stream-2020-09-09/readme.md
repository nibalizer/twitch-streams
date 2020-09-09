# 2020-09-09

## Summary

- We deployed apps written in the top four languages to IBM Cloud Kubernetes Service:
- Python - https://github.com/IBM/python-flask-app
- PHP - Default Laravel Blog Tutorial w/ Dockerfile below
- Java - https://github.com/nibalizer/hello-spencer
- Javascript - https://github.com/IBM-Cloud/get-started-node

## Announcements:

- 

## New Business:

-  Deploy to kubernetes using the top 4 languages

## If there is time:

-

## Commands

```
apt install php-bcmath php-ctype php-fileinfo php-json php-mbstring php-pdo php-tokenizer php-xml
kubectl run -i --tty poke2-`date +%s` --image=nibalizer/utilities --restart=Never -- sh
k port-forward svc/lang-php 5000:5000 --address 0.0.0.0
php artisan serve --host=0.0.0.0 --port=8181
```

## Links

- https://insights.stackoverflow.com/survey/2020#technology-what-languages-are-associated-with-the-highest-salaries-worldwide
- https://redmonk.com/sogrady/2020/02/28/language-rankings-1-20/
- https://github.com/nibalizer/hello-spencer
- https://github.com/IBM-Cloud/get-started-node
- https://github.com/IBM/nodejs-starter
- https://github.com/IBM/python-flask-app
- https://github.com/IBM/nodejs-express-app
- https://www.studentstutorial.com/laravel/hello-world
- https://blog.hashvel.com/posts/create-hello-world-in-laravel/
- https://blog.hashvel.com/series/laravel-beginner/
- https://blog.hashvel.com/posts/how-to-install-laravel-5-6-with-xampp-on-windows/
- https://github.com/niwasawa/php-laravel-hello-world
- https://eev.ee/blog/2012/04/09/php-a-fractal-of-bad-design/
- https://stitcher.io/blog/php-in-2019
- https://stitcher.io/blog/php-in-2019
- https://laravel.com/
- https://laravel.com/docs/8.x#installing-laravel
- https://getcomposer.org/
- https://stackoverflow.com/questions/28956911/how-can-i-access-my-laravel-app-from-another-pc
- https://stackoverflow.com/questions/28956911/how-can-i-access-my-laravel-app-from-another-pc
- https://www.digitalocean.com/community/tutorials/how-to-set-up-laravel-nginx-and-mysql-with-docker-compose
- https://buddy.works/guides/laravel-in-docker#docker-file-details
- https://buddy.works/
- https://github.com/docker-library/php/issues/880
- https://docs.oracle.com/cd/E37670_01/E75728/html/section-a4v_thh_r5.html#:~:text=If%20you%20specify%20the%20%2D%2D,are%20available%20to%20the%20host.
- https://quay.io/repository/
- https://quay.io/user/nibalizer
- https://kubernetes.io/docs/concepts/services-networking/connect-applications-service/
- https://spring.io/
- https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.18/#listmeta-v1-meta
- https://cloud.ibm.com/docs/containers?topic=containers-ingress_annotation
- https://cloud.ibm.com/docs/containers?topic=containers-ingress_annotation#location-snippets
- https://cloud.ibm.com/docs/containers?topic=containers-ingress_annotation#rewrite-path
