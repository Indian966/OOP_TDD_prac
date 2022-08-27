# zamface_preinterview

## 1. 코딩은 언제 시작 하셨는지요?
코딩은 대학교에 입학하면서 시작했습니다.
 
## 2. Github등에 가장 지원자님의 설계와 구조, 코드를 파악할수 있는 프로젝트가 있는지요? (개인코드면 더 좋습니다.)
https://github.com/Indian966/Django_recruting_developer 
 
## 3. 간단한 링크드 리스트나 해시테이블 구현 하는 코드 가능 하신지요?
 ```
class Node:
def __init__(self, data, next=None) :
self.data = data
self.next = next
 
node1 = Node(1)
 
print(node1.data, node1.next)
=>  1 None
 
node2 = Node(2)
 
print(node2.data)
=> 2
print(node1.next.data)
=> 2
 ```
 
## 4. 알고리즘과 코드 학습을 꾸준히 하시는지요?
주로 깃허브나 개인 블로그에 올라온 코드를 보고 리뷰 하듯이 공부하는 편입니다.
특히 현재 진행중인 프로젝트를 어떻게 더 발전시킬 수 있는지에 대해 고민합니다.
 
## 5. 가장 자신있게 보여줄 코드가 별도로 잇으신지요?
https://github.com/Indian966/Django_recruting_developer 
 
## 6. 하루에 코딩과 학습을 얼마나 하시는지요?
구직 활동을 하면서 코딩 이외에 시간을 쓰는 일이 많아졌지만 
하루에 최소 2시간은 코딩을 하는 편입니다.
 
## 7. 지난 6개월간 보신 기술서적이 무엇이 있으신지요?
주로 Django와 Go, Gunicon에 관한 문서를 보았습니다. 
 
## 8. 좋은 코드를 만드는데 가장 신경 쓰는 부분이 어느 부분인지요?
버그 발생에 대한 부분입니다.
좋은 코드란 개발자가 정해놓은 기능 이외에는 절대 동작하면 안된다고 생각합니다. 
 
## 9. Django Admin 개발 하시게 됩니다. 문제가 없을런지요?  
문제 없습니다.
 
## 10. 비동기 모델을 잘 이해하고 계신지요?
사실 비동기 모델에 관한 경험이 적은 편입니다.
과거에 DB에서 데이터를 받아 채팅방에 전달하는 기능을 만든적이 있습니다만
시간이 좀 지나서 다시 공부가 필요합니다.
 
## 11. 장고 개발시 View에서 template과 js 코드의 구조화를 어떻게 가져가는게 좋다고 생각하시는지요?
서로 나누어 관리하는것이 효율적이라고 생각합니다.
그 이유는 template내에 있는 html은 서버에서 요청이 있을때마다 전달하지만
JS는 변경이 있기 전까지는 전달하지 않기 때문입니다.

