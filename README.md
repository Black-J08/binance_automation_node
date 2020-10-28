# binance_automation

For Reference Only
1. Clone the repository
```git clone https://github.com/Black-J08/binance_automation.git```

2. Install ```pipenv``` to create python virtual environment
```pip install pipenv```

3. Move into ```binance_automation``` directory

4. Create a python virtual environment
```pipenv shell```

5. Install all dependencies
```pipenv install```

6. Place ```firebase-adminsdk-serviceAccountKey.json``` in root directory

7. Create a ```init-firebase.js``` file in ```/static/js``` folder with the following content. (Replace with your firebase project's config)
```
var firebaseConfig = {
    apiKey: "AIzaSyDOCAbC123dEf456GhI789jKl01-MnO",
    authDomain: "myapp-project-123.firebaseapp.com",
    databaseURL: "https://myapp-project-123.firebaseio.com",
    projectId: "myapp-project-123",
    storageBucket: "myapp-project-123.appspot.com",
    messagingSenderId: "65211879809",
    appId: "1:65211879909:web:3ae38ef1cdcb2e01fe5f0c",
    measurementId: "G-8GSGZQ44ST"
};

firebase.initializeApp(firebaseConfig);
const auth = firebase.auth();

```

8. Start the server 
```python run.py```
