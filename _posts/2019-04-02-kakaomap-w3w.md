---
layout: post
title: "카카오맵 x w3w (what3words)"
date: 2019-04-02 11:35:58 +0900
category: review
excerpt: "카카오맵에 탑재된 what3words, 지구를 3m x 3m 단위로 쪼개 세 단어로 주소를 붙이는 신 좌표체계를 소개합니다."
---

> 💡 이 글은 밍피디의 티스토리(cfdf.tistory.com)로부터 마이그레이션된 글입니다.
{: .migration-notice}

지도앱 많이들 쓰실텐데요. 국내에선 대부분 카카오맵이나 네이버지도를 사용하실거라 생각됩니다.

이번에 카카오맵이 업데이트가 되었는데요. 업데이트 내역을 살펴보았습니다.

![구글 플레이 업데이트 내역에 쓰여있는 What3Words 관련 내용](/assets/img/tistory/0038_01.png)
<p class="caption" style="font-size: 0.85em; color: gray; text-align: center; margin-top: 4px;"><i>구글 플레이 업데이트 내역에 쓰여있는 What3Words 관련 내용.</i></p>

~~(iOS는 심사중이라고 하네요.)~~ 2019년 4월 8일 (월) 오후 기준, iOS도 업데이트 되었습니다.


---


### What3Words?

<img src="/assets/img/tistory/0038_02.gif" alt="위치마다 세 단어가.." style="display: block; width: 320px; max-width: 100%; margin: 0 auto; border-radius: 10px;">
<p class="caption" style="font-size: 0.85em; color: gray; text-align: center; margin-top: 4px;"><i>위치마다 세 단어가..</i></p>

위를 보면 알 수 있듯이 세 단어로 표현되는 신 좌표체계입니다. 지구를 3㎡ 단위로 조각을 냅니다. (총 57조 조각이라고 합니다.) 그리고 그 조각에 3단어로 이름을 붙입니다. 그게 끝입니다.

[https://what3words.com/](https://what3words.com/)

현재 **20개 이상의 언어를 지원**합니다. 내부적으로 데이터 구조를 최적화했기 때문에 키워드 데이터가 **20MB 정도**밖에 안 한다고 합니다. 또, 비슷한 단어는 근처에 존재하지 않고 아주 멀리 떨어져있게 설계하여 **헷갈림 포인트를 줄였**습니다. (근데 그게 영어 기준인지, 다른 언어도 그런 건지는 잘 모르겠습니다.)

이것을 어디에 사용할 수 있을까요?

- (한국은 아니지만) 주소체계가 미비한 곳에서 사용할 수 있습니다.
- 재난 상황에서도 유용하게 사용할 수 있습니다.
- 더 나아가 자율주행 등의 새로운 산업에서도 사용할 수 있겠습니다.
- 맘만 먹으면 실생활에서도 사용 가능합니다. "현백 10층 힌트,지냈다,톡톡으로 와"

아래는 제가 좋아하는 유튜버 JM님이 이것에 대해 소개했던 영상인데요. 재밌게 설명을 잘 해주셔서 첨부합니다.

<div class="video-container" style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; margin: 20px 0;">
  <iframe src="https://www.youtube.com/embed/RFRmSwIiiF8" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>

(다만 이분은 "미래의 주소체계"라고 말씀하시지만 개인적으로는 "미래의 좌표체계"가 더 맞는 것 같습니다.)


---


### 카카오맵 x what3words

그런데 이것이 카카오맵에 탑재되었습니다.

![특정 위치를 길게 누르면 W3W 기능을 사용할 수 있습니다.](/assets/img/tistory/0038_03.png)
<p class="caption" style="font-size: 0.85em; color: gray; text-align: center; margin-top: 4px;"><i>특정 위치를 길게 누르면 W3W 기능을 사용할 수 있습니다.</i></p>

다른 곳에 공유도 쉽게 가능한데요. 공유하기 버튼 선택 후 클립보드로 복사하면 아래와 같은 텍스트가 복사됩니다.

![공유되는 텍스트](/assets/img/tistory/0038_04.png)
<p class="caption" style="font-size: 0.85em; color: gray; text-align: center; margin-top: 4px;"><i>공유되는 텍스트.</i></p>

W3W 좌표로 공유됨을 알 수 있습니다.

![세 단어 좌표로 검색도 가능합니다.](/assets/img/tistory/0038_05.png)
<p class="caption" style="font-size: 0.85em; color: gray; text-align: center; margin-top: 4px;"><i>세 단어 좌표로 검색도 가능합니다.</i></p>

검색도 가능한데요. 앞에 /// (슬래시 3개)를 붙여서 단어 좌표를 입력하면 검색도 가능합니다.


---


### 마치며

이런 실험적인 기능을 메이저 회사가 나서서 도입했다는 점은 칭찬할 포인트인 것 같습니다.

[\[카카오맵APP\] what3words 기능 카카오맵 반영](https://kakaomap.tistory.com/238)

+++++++++++

최근에 JM님이 이것에 대한 영상을 올리셔서 추가로 첨부합니다.

<div class="video-container" style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; margin: 20px 0;">
  <iframe src="https://www.youtube.com/embed/KHi4xQpwohY" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
</div>
