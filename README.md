# 2024 SSF Layer7
## 2024 선린인터넷고등학교 소프트웨어 나눔축제 Layer7

크롬 확장 프로그램 적용(Victim) : `chrome://extension` 에서 extension 폴더 로드<br>
<img width="406" alt="Screenshot 2024-07-25 at 8 25 11 PM" src="https://github.com/user-attachments/assets/411fc711-1310-4b8e-ac16-6c52c4a0c4c9"><br>
Load unpacked<br>
<img width="433" alt="Screenshot 2024-07-25 at 8 26 01 PM" src="https://github.com/user-attachments/assets/b0c8d9ae-b2cf-41d0-94af-53acd03d7fde"><br>
불러온거 확인

서버(Attacker) : python3 그리고 flask 필요. `python3 main.py`
<img width="624" alt="Screenshot 2024-07-25 at 8 26 43 PM" src="https://github.com/user-attachments/assets/e15246aa-fcc5-4c4e-bc27-d01daf369660"><br>
서버 켜짐

서버와 확장 프로그램이 켜진 상태로 사이트에 들어가서 키 누를 시 아래와 같이 서버에서 확인 가능
<img width="524" alt="Screenshot 2024-07-25 at 8 27 10 PM" src="https://github.com/user-attachments/assets/a190ca05-4353-44c3-8bfb-3030afe7ba87"><br>
로그:<br>
<img width="659" alt="Screenshot 2024-08-22 at 4 22 19 PM" src="https://github.com/user-attachments/assets/acf2a11f-13f9-4276-b3bb-bb02abcd1424">

실제 사용 시 크롬 확장 프로그램 코드에 들어가있는 서버 주소 변경 필요