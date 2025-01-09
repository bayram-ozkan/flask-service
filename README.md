
# Uygulamayı kubernetes üzerinden deploy ve ingress

# Adımlar: 
1. Uygulamayı bir Kubernetes cluster dağıtın. 
2. Dağıtım için kubectl, Helm veya Kustomize gibi bir araç kullanın. 
3. Uygulamanın bir LoadBalancer veya Ingress aracılığıyla erişilebilir olduğundan emin olun. 
4. Uygulama için rolling güncellemelerini gösterin.


## yaml dosyalarımızın bulunduğu dizine geçiş yapalım ve çalıştıralım .

```
cd kubernetes/
```

## Dizindeki tüm dosyaları çalıştıralım 
```
kubectl  apply -f . 
```

## versiyon history
```
kubectl rollout history deployment  task1-app
```

##  Versiyon değiştirme .default versiyondan v1 versiyona geçiş yapıyoruz
```
kubectl  set image deployment/task1-app task1-http-server=bbw0r1d/task1-http-server:v1
```

## rollout un durumunu gösterir.
```
kubectl rollout status deployment rolldeployment -w
```

## En son rollout un açıklamasını değiştirir.   
```
kubectl annotate deployment task1-app kubernetes.io/change-cause="Updated task1-http-server default to v1"
```

## En son deployment version  a geri döner
```
kubectl rollout undo deployment task1-app   
```


#  Deployment ın belirtilen  revizyone(2) geri döner
```
kubectl rollout undo deployment task1-app  --to-revision 2
```


