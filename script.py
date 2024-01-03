from dvclive import Live
with Live(save_dvc_exp=True) as live:
  for epoch in range(5):
    live.log_metric("accuracy", 5)
    live.log_metric("loss", 5)
    live.next_step()