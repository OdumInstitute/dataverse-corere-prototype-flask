export FN_AUTH_REDIRECT_URI=http://localhost:5000/google/auth
export FN_BASE_URI=http://localhost:5000
export FN_CLIENT_ID=GOOGLE_CLIENT_ID_GOES_HERE
export FN_CLIENT_SECRET=GOOGLE_CLIENT_SECRET_GOES_HERE

export FN_GITHUB_CLIENT_ID=GITHUB_CLIENT_ID_GOES_HERE
export FN_GITHUB_CLIENT_SECRET=GITHUB_CLIENT_SECRET_GOES_HERE

export FLASK_APP=index.py
export FLASK_DEBUG=1
export FN_FLASK_SECRET_KEY=RANDOMSECRETdsjaldsajio

export DATABASE_URL="postgresql://localhost/core"

if [[ -z "${APP_DOCKER}" ]]; then
   python -m flask run --host=0.0.0.0
else
   python -m flask run
fi
