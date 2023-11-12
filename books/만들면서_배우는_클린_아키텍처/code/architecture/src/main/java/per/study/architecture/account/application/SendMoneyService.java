package per.study.architecture.account.application;

import lombok.RequiredArgsConstructor;
import org.springframework.transaction.annotation.Transactional;
import per.study.architecture.account.application.port.in.SendMoneyCommand;
import per.study.architecture.account.application.port.in.SendMoneyUseCase;
import per.study.architecture.account.application.port.out.LoadAccountPort;
import per.study.architecture.account.application.port.out.UpdateAccountStatePort;

@RequiredArgsConstructor
@Transactional
public class SendMoneyService implements SendMoneyUseCase {

    private final LoadAccountPort loadAccountPort;
    private final UpdateAccountStatePort updateAccountStatePort;

    @Override
    public boolean sendMoney(SendMoneyCommand command) {
        return false;
    }
}
