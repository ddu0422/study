package per.study.architecture.account.application.port.in;

import jakarta.validation.constraints.NotNull;
import lombok.Builder;
import per.study.architecture.share.SelfValidating;

@Builder
public class SendMoneyCommand extends SelfValidating<SendMoneyCommand> {

    @NotNull
    private String name;

    public SendMoneyCommand(String name) {
        this.name = name;
        validateSelf();
    }
}
