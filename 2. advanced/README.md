# Advanced

이번 실습에서는 애저에서 가장 기본적인 형태의 웹 애플리케이션을 배포하는 방법에 대해 알아보도록 하겠습니다. 가상 머신에 웹 애플리케이션을 배포하고 웹 애플리케이션의 데이터를 관리하기 위한 SQL 데이터베이스를 구성해 보도록 하겠습니다. 부하 분산 장치의 프런트 엔드 IP를 웹 애플리케이션을 진입점으로 사용하고 가상 머신을 백 엔드 풀로 사용합니다. 이렇게 구성하면 웹 애플리케이션을 논리적으로 격리할 수 있으며, 추후 애플리케이션의 확장을 고려한 아키텍처를 설계할 수 있습니다.

![Untitled](images/Untitled.png)

### 실습 내용

- 가상 네트워크 만들기
- 부하 분산 장치 만들기
- NAT 게이트웨이 만들기
- 웹 애플리케이션 배포
    - 가상 머신 만들기
    - 베스천 설정
    - 웹 애플리케이션 배포
    - 배포 테스트
- SQL 데이터베이스 연동
    - SQL 데이터베이스 서버 만들기
    - SQL 데이터베이스 만들기
    - 데이터베이스 엔드포인트 만들기
    - SQL 데이터베이스 연동

## 가상 네트워크 만들기

![Untitled](images/Untitled%201.png)

1. 왼쪽 상단 검색창에서 `가상 네트워크` 입력하여 가상 네트워크 화면으로 이동합니다.
2. `만들기` 버튼을 클릭합니다.
3. 아래와 같이 구성하고 `다음: IP 주소` 버튼을 클릭합니다.
    
    ![Untitled](images/Untitled%202.png)
    
    - 구독 : 생성한 구독 선택
    - 리소스 그룹 : 새로 만들기 버튼 클릭 후, BasicWorkshopRG 입력하고 `확인` 버튼 클릭
    - 이름 : BasicVNet
    - 지역 : KoreaCentral

4. 아래와 같이 구성된 것을 확인하고 `검토 + 만들기` 버튼을 클릭합니다.
    
    ![Untitled](images/Untitled%203.png)
    

5. `만들기` 버튼을 클릭하여 가상 네트워크를 생성합니다.

## 부하 분산 장치 만들기

![Untitled](images/Untitled%204.png)

1. 왼쪽 상단 검색창에서 `부하 분산 장치` 입력하여 부하 분산 장치 화면으로 이동합니다.
2. `만들기` 버튼을 클릭합니다.
3. 아래와 같이 구성합니다.
    
    ![Untitled](images/Untitled%205.png)
    
    - 구독 : 생성한 구독 선택
    - 리소스 그룹 : BasicWorkshopRG
    - 이름 : sample-app-lb
    - 지역 : Korea Central
    - SKU : 표준
    - 형식 : 공개
    - 계층 : 지역
4. `다음: 프런트 엔드 IP 구성` 버튼을 클릭합니다.
5. `프런트 엔드 IP 구성 추가` 버튼을 클릭하고 아래와 같이 구성 후, `추가` 버튼을 클릭합니다.
    
    ![Untitled](images/Untitled%206.png)
    
    - 이름 : FrontendIP
    - IP 버전 : IPv4
    - IP 유형 : IP 주소
    - 공용 IP 주소 : `새로 만들기` 버튼 클릭
        - 이름 : APPPIP

6. `다음: 백 엔드 풀` 버튼을 클릭하고 `백 엔드 풀 추가`를 클릭합니다.
7. 아래와 같이 구성하고 `저장` 버튼을 클릭합니다.
    
    ![Untitled](images/Untitled%207.png)
    
    - 이름 : backend-pool
    - 가상 네트워크 : BasicVNet(BasicWorkshopRG)
    - 백 엔드 풀 구성 : NIC

8. `다음: 인바운드 규칙` 버튼을 클릭합니다.
9. 부하 분산 규칙을 생성하여 적용해 보도록 하겠습니다. `부하 분산 규칙 추가` 버튼을 클릭하고 다음과 같이 구성합니다.
    
    ![Untitled](images/Untitled%208.png)
    
10. 상태 프로브는 백 엔드 풀의 정상 상태를 확인합니다. 상태 프로브에서 `새로 만들기`를 클릭하고 다음과 같이 설정하고 `확인` 버튼을 클릭합니다.

![Untitled](images/Untitled%209.png)

11. TodoRule이 정상적으로 추가된 것을 확인한 뒤, `검토 + 만들기` 버튼을 클릭하고 `만들기` 버튼을 클릭하여 부하 분산 장치를 생성합니다.

## 웹 애플리케이션 배포

### 가상 머신 만들기

![Untitled](images/Untitled%2010.png)

1. 왼쪽 상단 검색창에서 `가상 머신` 입력하여 가상 머신 화면으로 이동합니다.
2. `만들기` 버튼을 클릭하고 Azure 가상 머신을 선택합니다.
    
    ![Untitled](images/Untitled%2011.png)
    

3. 아래와 같이 구성하고 `네트워킹` 탭을 선택하거나 `다음: 디스크, 다음: 네트워킹`을 차례로 선택합니다.
    
    ![Untitled](images/Untitled%2012.png)
    
    - 구독 : 생성한 구독 선택
    - 리소스 그룹 : BasicWorkshopRG
    - 가상 머신 이름 : appVM
    - 지역 : (Asia Pacific) Korea Central
    - 가용성 옵션 : 인프라 중복이 필요하지 않습니다.
    - 보안 유형 : 표준
    - 관리자 계정 : 암호
        - 사용자 이름 : azureuser
        - 암호 : Workshop12!@
4. 네트워킹 탭에서 다음 정보를 선택하거나 입력합니다.
    
    ![Untitled](images/Untitled%2013.png)
    
    - 가상 네트워크 : BasicVNet
    - 서브넷 : `서브넷 구성 관리` 클릭
        - `서브넷` 버튼 클릭
        - 이름 : applicationSubnet
        - 서브넷 주소 범위 : 10.0.1.0/24
        - `저장` 버튼 클릭
        - 오른쪽 상단 `x` 버튼 클릭
        - `applicationSubnet` 선택
    - 공용 IP : 없음
    - NIC 네트워크 보안 그룹 : 기본

5. 부하 분산에서 `기존 부하 분산 솔루션 뒤에 이 가상 머신을 배치하겠습니까?` 체크박스를 클릭하고 아래와 같이 구성합니다.
    
    ![Untitled](images/Untitled%2014.png)
    
    - 부하 분산 옵션 : Azure Load Balancer
    - 부하 분산 장치 선택 : sample-app-lb
    - 백 엔드 풀 선택 : backend-pool

6. `검토 + 만들기` 버튼을 클릭하고 설정을 검토한 다음 `만들기`를 선택합니다. 

### 베스천 배포하기

강사의 가이드를 따라 1) 베스천 서비스 사용 혹은 2) 베스천 구성 을 택 1 하여 진행합니다.

**1) 베스천 서비스 사용**

1. `가상 머신 화면`에서 TodoVM1을 클릭하고, 왼쪽 `베스천` 메뉴를 클릭합니다.
2. `기본값을 사용하여 Azure Bastion …` ****버튼을 클릭합니다.
    
    ![Untitled](images/Untitled%2015.png)
    

**2) 베스천 구성 (인바운드 NAT 규칙)**

1. `부하 분산 장치` 화면에서 생선한 부하 분산 장치를 선택합니다.
2. 왼쪽 블레이드 메뉴에서 `설정 > 인바운드 NAT 규칙`을 클릭합니다.
3. `추가` 버튼을 클릭합니다.
4. 아래와 같이 구성 후, 저장 버튼을 클릭합니다.
    
    ![Untitled](images/Untitled%2016.png)
    

### 웹 애플리케이션 배포

베스천을 사용하여 웹 애플리케이션을 배포해 보도록 하겠습니다.

1. 베스천 접속
    1. 베스천이 생성되면 아래 정보를 입력하고 연결 버튼을 클릭합니다.
        
        ![Untitled](images/Untitled%2017.png)
        
    2. 로컬 컴퓨터의 PowerShell, 터미널 등을 사용해 아래 명령어를 사용하여 VM에 접속합니다.
        
        ```bash
        ssh azureuser@<부하 분산 장치의 Frontend IP>
        ```
        
2. 샘플 애플리케이션은 Docker Image로 구성되어 있습니다. VM에 Docker Runtime을 구성합니다.
    
    ```bash
    # Add Docker's official GPG key:
    sudo apt-get update
    sudo apt-get install ca-certificates curl
    sudo install -m 0755 -d /etc/apt/keyrings
    sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
    sudo chmod a+r /etc/apt/keyrings/docker.asc
    
    # Add the repository to Apt sources:
    echo \
      "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
      $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
      sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    sudo apt-get update
    ```
    
    ```bash
    sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
    ```
    
3. 샘플 애플리케이션 이미지를 가져옵니다.
    
    ```bash
    sudo docker pull sheltersune/addressbook
    ```
    
4. 이미지를 실행합니다.
    
    ```bash
    sudo docker run -d -p 80:8000 sheltersune/addressbook
    ```
    

### 배포 테스트

1. `부하 분산 장치 화면`에서 생성한 `sample-app-lb`에서 왼쪽 `프런트 엔드 IP` 구성 메뉴를 클릭합니다.
    
    ![Untitled](images/Untitled%2018.png)
    
2. 새 탭에서 해당 퍼블릭 아이피를 통해 정상적으로 웹 애플리케이션에 접속되는 것을 확인합니다.
    
    ![Untitled](images/Untitled%2019.png)
    

## SQL 데이터베이스 연동

### SQL 데이터베이스 서버 만들기

![Untitled](images/Untitled%2020.png)

1. 왼쪽 상단 검색창에서 `SQL Server` 입력하여 SQL Server 화면으로 이동합니다.
2. `만들기` 버튼을 클릭합니다.
3. 아래와 같이 구성하고 `검토 + 만들기` 버튼을 클릭합니다.
    
    ![Untitled](images/Untitled%2021.png)
    
    - 서버 이름 : basic-workshop-<name>
    - 위치 : (Asia Pacific) 한국 중부
    - 인증 방법 : SQL 인증 사용
        - 서버 관리자 로그인 : db-admin
        - 암호 : Workshop12!@

4. 리소스가 생성되면 `리소스로 이동` 버튼을 클릭합니다.

### SQL 데이터베이스 만들기

1. 왼쪽 상단 검색창에서 `SQL 데이터베이스` 입력하여 SQL 데이터베이스 화면으로 이동합니다.
2. `만들기` 버튼을 클릭합니다.
    
    ![Untitled](images/Untitled%2022.png)
    

3. 아래와 같이 구성합니다.
    - 구독 : 생성한 구독 선택
    - 리소스 그룹 : BasicWorkshopRG
    - 데이터베이스 이름 : basic-workshop
    - 서버 : basic-workshop

4. 나머지 설정은 그대로 두고, `검토+만들기` 버튼을 클릭합니다. 다음과 같은 화면이 뜨면 구성 내용을 확인하고 `만들기` 버튼을 클릭합니다.
    
    ![Untitled](images/Untitled%2023.png)
    

### 데이터베이스 프라이빗 엔드포인트 만들기

1. 왼쪽 메뉴에서 `네트워킹`을 클릭하고 `프라이빗 액세스` 탭을 클릭합니다.
2. `프라이빗 엔드포인트 만들기`를 클릭합니다.
    
    ![Untitled](images/Untitled%2024.png)
    

3. 아래와 같이 구성 후, `다음: 리소스 >` 버튼을 클릭합니다.
    
    ![Untitled](images/Untitled%2025.png)
    
    - 구독 : 생성한 구독 선택
    - 리소스 그룹 : BasicWorkshopRG
    - 인스턴스 정보
        - 이름 : DBPrivateEP
        - 네트워크 인터페이스 이름 : DBPrivateEP-nic (자동생성)
        - 지역 : 한국 중부

4. 대상 하위 리소스가 자동으로 `sqlServer`로 선택되면 `다음: 가상 네트워크 >` 버튼을 클릭합니다.
5. 아래와 같이 설정한 뒤 나머지 설정은 그대로 두고 프라이빗 엔드포인트를 생성합니다.
    
    ![Untitled](images/Untitled%2026.png)
    
    - 가상 네트워크 : BasicVNet(basicworkshoprg)
    - 서브넷 : default

### SQL 데이터베이스 연동

1. 리소스가 생성되면 왼쪽 메뉴에서 `개요`를 클릭하고 `서버 이름`을 복사합니다.
    
    ![Untitled](images/Untitled%2027.png)
    

2. 전 단계에서 띄워둔 웹 페이지(부하 분산 장치의 프런트 엔드 IP)로 접속하고 `Connect to DB` 탭을 클릭합니다.
    
    ![Untitled](images/Untitled%2028.png)
    

3. 아래와 같이 구성 후, `Connect` 버튼을 클릭합니다.
    
    ![Untitled](images/Untitled%2029.png)
    
    - Server Name : SQL 데이터베이스 서버 이름
    - Server Admin : db-admin
    - Password : Workshop12!@

4. 정상적으로 연결이 완료되면, 다시 List 화면으로 돌아와서 기능들을 테스트합니다.
    
    ![Untitled](images/Untitled%2030.png)
    

수고하셨습니다. 감사합니다🙂