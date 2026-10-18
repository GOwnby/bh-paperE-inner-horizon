# Code for Paper E
ori_model.py  - Ori thin-null-shell model for a general closure (eqs. 3-5); make_results.py - validation tables, closure classes, figure;
evap_coupling.py / evap_table.py - evaporation-integrated inner-horizon exponent (Sec. 5). Python 3, numpy, scipy, matplotlib.
Run:  cd code && python3 make_results.py && python3 evap_table.py   (about 5 min)


nonlinear/ - double-null Einstein-NED-scalar evolution used in Section 6 (build line, one script per result and wall times in nonlinear/README.md).
ori_model.py also contains the closure 'hn' (additive Hayward-NED, G = M_N'(r)) used for the comparison.
* Event-horizon-regular data, kernel and ray integration are now Paper G (`../../paperG_late_time_method`); the code stays in eh_init/ (see eh_init/README.md).  Paper E uses from it: check_field_equations.py, conserv_num.py, e15_extend.py, raylib_sc.py + e8_semiclassical.py (Hawking-flux anomaly term, Section 6.8) and e12_ratio.py (flux to v=420).
