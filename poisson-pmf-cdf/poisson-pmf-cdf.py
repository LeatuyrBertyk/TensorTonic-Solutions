import numpy as np

def poisson_pmf_cdf(lam, k):
    """
    Compute Poisson PMF and CDF.
    """
    # Compute pmf:
    log_pmf = -lam + k*np.log(lam) - np.sum(np.log(np.arange(1,k+1)))
    pmf = np.exp(log_pmf)

    # Compute_cdf:
    cdf_log_i = np.array([-lam + i*np.log(lam) - np.sum(np.log(np.arange(1,i+1))) for i in range(0,k+1)])
    cdf_i = np.exp(cdf_log_i)
    cdf = np.sum(cdf_i)

    return pmf, cdf