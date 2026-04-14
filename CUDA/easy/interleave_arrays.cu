#include <cuda_runtime.h>

__global__ void interleave_kernel(const float* A, const float* B, float* output, int N) {
    int i = threadIdx.x + blockDim.x * blockIdx.x;
    if (i < N) {
        // cue: number of threads = N, each thread processes one element from A and one from B
        // can use 2N threads where each thread does one write (faster), but would cause
        // more divergent execution and more memory accesses (%2 operation to determine which
        // array to read from - warps would be split into two groups, one for A and one for B)
        output[i * 2] = A[i];
        output[(i * 2) + 1] = B[i];
    }
}

// A, B, output are device pointers (i.e. pointers to memory on the GPU)
extern "C" void solve(const float* A, const float* B, float* output, int N) {
    int threadsPerBlock = 256;
    int blocksPerGrid = (N + threadsPerBlock - 1) / threadsPerBlock;

    interleave_kernel<<<blocksPerGrid, threadsPerBlock>>>(A, B, output, N);
    cudaDeviceSynchronize();
}
