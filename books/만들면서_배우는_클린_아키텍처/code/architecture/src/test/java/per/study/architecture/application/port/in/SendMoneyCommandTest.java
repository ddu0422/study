package per.study.architecture.application.port.in;

import org.junit.jupiter.api.Test;
import per.study.architecture.account.application.port.in.SendMoneyCommand;

public class SendMoneyCommandTest {

    @Test
    void test() {
        SendMoneyCommand.builder()
            .name(null)
            .build();
    }
}
