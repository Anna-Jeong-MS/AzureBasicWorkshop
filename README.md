# Azure Basic Workshop

Azure Basic Workshop은 Azure 인프라의 핵심 서비스를 직접 실습해보는 Hands-on Lab입니다.  
가상 네트워크, 가상 머신, SQL Database, 부하 분산 장치(Load Balancer) 등을 활용하여  
실제 웹 애플리케이션을 배포하고, 확장 가능한 구조로 구성해봅니다.

---

## 실습 목표

- Azure 환경에서 VM, 네트워크, 데이터베이스 구성 실습
- 웹 애플리케이션 배포 및 외부 접속 구성
- 부하 분산 및 가용성 고려 아키텍처 설계

---

## 실습 전 준비사항

- Microsoft Azure 구독 계정
- Azure Portal 접속 환경 (웹 브라우저)
- SSH 또는 RDP 접속 가능한 로컬 장치
- 기본적인 클라우드 컴퓨팅 이해

---

## 추가 실습: VMSS 구성

워크숍 기본 실습을 마친 후 다음 항목들을 통해 실습을 확장해 볼 수 있습니다:

- **Load Balancer** 설정:  
  - 프론트엔드 IP 주소(front‑end IP)를 웹 애플리케이션 진입점으로 설정  
  - 가상 머신들을 백엔드 풀(backend pool)로 구성하여 트래픽 분산  
- 논리적 격리(Logical Isolation) 및 보안 그룹 구성: 애플리케이션 계층과 데이터 계층 간의 접근 통제  
- 확장성(Scalability) 고려: VM을 백엔드 풀로 구성함으로써 추가 VM 추가/제거 용이한 구조 설계

---

## 피드백 & 기여

- 개선 아이디어, 오류 제보는 [Issues](https://github.com/Anna-Jeong-MS/AzureBasicWorkshop/issues) 탭을 활용해 주세요.
- Pull Request를 통한 기여도 언제든지 환영합니다!

---

> 본 프로젝트는 Azure 입문자를 위한 학습용 워크숍입니다.  
> 운영자: [@Anna-Jeong-MS](https://github.com/Anna-Jeong-MS)