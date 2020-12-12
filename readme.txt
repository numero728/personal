수신 양호

# 연동 확인 김채정

# 미니프로젝트 관련 환경
- 배포 후 클라이언트측 화면 확인 위해 임시적으로 강사님이 제공한 fabfile.py 사용
- 가상머신 이름: miniproject
- key pair 이름: miniproject_key
- DNS 이름: Configure
- IP: 40.76.38.92

- DB 인스턴스_식별자: personaldb
- 사용자 이름: admin
- pw: pnudb960726!
- host: cepsu2i8bkn5.ap-northeast-2.rds.amazonaws.com
# 서버 최초 배포 후 apache2 default page 설정
# ssh 접속 후
1) /etc/apache2/sites_available 디렉토리로 이동
2) sudo a2dissite 000-default.conf
3) sudo systemctl reload apache2

# 크롬 브라우저 설치
1. sudo wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
2. dpkg로 deb 파일 install
3. dpkg 명령 수행 위한 requirements 충족 필요
3.1. dppk 명령 수행 이후 -> dependencies 언급됨
3.2. sudo apt-get -f install

# 크롬 드라이버 설치
1. wget -N https://chromedriver.storage.googleapis.com/87.0.4280.88/chromedriver_linux64.zip
2. unzip으로 압축 해제
