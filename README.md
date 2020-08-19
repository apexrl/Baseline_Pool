# Baseline_Pool
A pool that contains previous baseline results along with their plotters run by us.

One method per directory.

## model_based

Contains some model-based baselines results on mujoco.

|  Algs   | Envs  | Curve Data | Sampled Trajs | Plot Scripts |
|  ----  | ----  | ----  | ----  | ----  |
| BMPO  | Ant, Hopper, Hopperrnt, Pendululm, Walker2d, Walker2drnt | Y | N | Y
| MBPO  | Ant, Hopper, Hopperrnt, Pendululm, Walker2d, Walker2drnt | Y | N | Y
| PETS  | Ant, Hopper, Hopperrnt, Pendululm, Walker2d, Walker2drnt | Y | N | Y
| SLBO  | Ant, Hopper, Hopperrnt, Pendululm, Walker2d, Walker2drnt | Y | N | Y
| SAC  | Ant, Hopper, Hopperrnt, Pendululm, Walker2d, Walker2drnt | Y | N | Y

Contributed by Hang Lai.

## imitation learning

Contains imitation learning baseline expert trajs, results on mujoco.

|  Algs   | Envs  | Curve Data | Sampled Trajs | Plot Scripts |
|  ----  | ----  | ----  | ----  | ----  |
| SAC  | Ant, Hopper, Humanoid, HalfCheetah, Walker2d, Swimmer | N | Y | N

Contributed by Minghuan Liu.
