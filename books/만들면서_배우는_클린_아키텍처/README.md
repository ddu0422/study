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

# 유스케이스 둘러보기

- 비즈니스 규칙을 검증할 책임
  - 비즈니스 규칙을 충족하면 유스케이스는 입력을 기반으로 어떤 방법으로든 모델의 상태를 변경한다.
    - 유효성 검증: 사용자가 올바르지 않은 값을 예방하는 규칙 (음수는 입력 불가)
    - 비즈니스 검증: 회사에서 정하는 규칙 (최대 OO만원까지 송금 가능) (도메인에서 검증하기)
  - 일반적으로 도메인 객체의 상태를 바꾸고 영속성 어댑터를 통해 구현된 포트로 이 상태를 전달해서 저장될 수 있게 한다.
  - 유스케이스는 또 다른 아웃고잉 어댑터를 호출할 수도 있다.
- 도메인 엔티티와 책임을 공유

# 입력 유효성 검증하기

- 입력 모델에서 입력 유효성을 검증한다.
- [Bean Validation API](https://beanvalidation.org)을 사용한다.
- 빌더 패턴 대신 IDE를 믿고 생성자를 직접 활용한다. -> (반대)

  - (Human Error) Parameter Type이 동일한 경우 개발자의 실수로 다른 컬럼에 들어갈 값과 바꿔서 넣을 수 있다.
  - Lombok을 활용하여 Builder Pattern을 구현하면 된다.
  - SelfValidating도 사용할 수 있으므로 문제가 되지 않는다.

  ```java
  @Builder
  public class SendMoneyCommand extends SelfValidating<SendMoneyCommand> {

    @NotNull
    private String name;

    public SendMoneyCommand(String name) {
        this.name = name;
        validateSelf();
    }
  }

  public class SendMoneyCommandTest {

    @Test
    void test() {
        SendMoneyCommand.builder()
            .name(null)
            .build();
    }
  }

  /*
  name: must not be null
  jakarta.validation.ConstraintViolationException: name: must not be null
  */
  ```
