import pathlib as pl
import flopy

# create single domain model equivalent to base parallel model in the MODFLOW 6 repo
name = "single"
ws_single = pl.Path(f"temp/{name}")
sim_base = flopy.mf6.MFSimulation(sim_name=name, sim_ws=ws_single)
tdis = flopy.mf6.ModflowTdis(sim_base)
ims = flopy.mf6.ModflowIms(sim_base, inner_dvclose=1e-8, outer_dvclose=1e-8)
gwf = flopy.mf6.ModflowGwf(sim_base, modelname=name)
dis = flopy.mf6.ModflowGwfdis(
    gwf,
    nrow=1,
    ncol=10,
    nlay=1,
    top=10.0,
    botm=-100.0,
    delr=100.0,
    delc=100.00,
)
npf = flopy.mf6.ModflowGwfnpf(gwf, icelltype=1, k=1.0)
ic = flopy.mf6.ModflowGwfic(gwf, strt=0.0)
chd = flopy.mf6.ModflowGwfchd(
    gwf, stress_period_data=[(0, 0, 0, 1.0), (0, 0, 9, 10.0)]
)
oc = flopy.mf6.ModflowGwfoc(
    gwf, head_filerecord=f"{name}.hds", saverecord=[("head", "all")]
)

sim_base.write_simulation()
success, buff = sim_base.run_simulation()
assert success, "flopy generated MODFLOW model did not run"

msg = "Successful testing of the class environment for Part 1"
print(msg)
