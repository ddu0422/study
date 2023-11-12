# Layerd Architecture의 문제점

- 서비스 계층이 비대해진다.
  - 많은 내용이 함축되어 있기 때문에 테스트를 진행하기 어렵다.
  - 영속성 계층에 많은 의존성을 지니게 된다.
- 동시 작업이 어려워진다.
  - 영속성 계층에 의존하기 때문에 서비스/웹 계층은 영속성 계층위에 만들어지기 때문에 영속성 계층이 가장 먼저 개발되어야 한다.

<br>

# Hexagonal Architecture

![hegagoanl-architecture](./images/hexagonal-architecture.png)

| 용어     | 설명                                             | 예시                        |
| -------- | ------------------------------------------------ | --------------------------- |
| Adapter  | Application과 상호작용하는 시스템                | Web, Database               |
| Port     | Application Core와 Adapter의 통신 수단           | Input Port, Output Port     |
| Use Case | Domain Entity와 상호작용하는 계층                | Use Case (SendMoneyUseCase) |
| Entity   | Application을 구성하기 위해 필요한 Dmoain Entity | Entity (Account)            |

```
account
ㄴ adapter
    ㄴ in
      ㄴ AccountController
    ㄴ out
      ㄴ persistence
        ㄴ AccountPersistenceAdapter
        ㄴ SpringDataAccountRepository
ㄴ application
  ㄴ port
    ㄴ in
      ㄴ SendMoneyUseCase
    ㄴ out
      ㄴ LoadAccountPort
      ㄴ UpdateAccountStatePort
  SendMoneyService
ㄴ domain
  ㄴ Account
  ㄴ Activity
```
