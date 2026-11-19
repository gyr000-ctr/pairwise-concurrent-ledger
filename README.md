# pairwise-concurrent-ledger

## 题面

多租户并发扣减额度时出现超发与重复入账：检查余额与扣减之间存在竞态未加锁；扣减非原子可被并发重复执行；同一请求重入未做幂等；失败后状态未回滚留下脏数据；并发下额度计数与流水不一致。ledger/account.py 是核心，tests/test_account.py 15个红。要修的是：临界区加锁保证检查与扣减原子；扣减操作原子化防重复执行；按请求标识做幂等去重；失败时回滚全部相关状态；保证额度计数与流水最终一致。

## 运行方式

```bash
python -m pytest tests -q
```

初始状态应为 `15 failed`，无 collection error；`tests/` 目录不可修改。

## 字段

- 所属领域：安全
- 子方向：漏洞检测与攻防
- 任务类型：Bugfix
- 语言/框架：Python 3, pytest
- 环境可复现等级：无外部依赖
