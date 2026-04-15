#include <cuda_runtime.h>

__global__ void geglu_kernel(const float* input, float* output, int halfN) {
    int i = threadIdx.x + blockDim.x * blockIdx.x;
    if (i < halfN) {
        output[i] = (input[i + halfN] / 2) * (1 + erf(input[i + halfN]/sqrt(2)));
        output[i] *= input[i];
    }
}

// input, output are device pointers
extern "C" void solve(const float* input, float* output, int N) {
    int halfN = N / 2;
    int threadsPerBlock = 256;
    int blocksPerGrid = (halfN + threadsPerBlock - 1) / threadsPerBlock;

    geglu_kernel<<<blocksPerGrid, threadsPerBlock>>>(input, output, halfN);
    cudaDeviceSynchronize();
}
