#define NOMINMAX
#include <windows.h>
#include <vector>
#include <string>
#include <fstream>
#include <algorithm>
#include <chrono>
#include <iostream>
#include <random>

// ——— Radix sort (LSD, non-negative) ——————————————————
void counting_sort_for_radix(std::vector<long long>& arr, long long exp) {
    size_t n = arr.size();
    std::vector<long long> output(n);
    int count[10] = {0};
    for (size_t i = 0; i < n; ++i)
        count[(arr[i] / exp) % 10]++;
    for (int i = 1; i < 10; ++i)
        count[i] += count[i - 1];
    for (size_t i = n; i-- > 0; ) {
        int d = (arr[i] / exp) % 10;
        output[--count[d]] = arr[i];
    }
    arr = std::move(output);
}
void radix_sort(std::vector<long long>& arr) {
    if (arr.empty()) return;
    long long maxv = *std::max_element(arr.begin(), arr.end());
    for (long long exp = 1; maxv / exp > 0; exp *= 10)
        counting_sort_for_radix(arr, exp);
}

// ——— Heap sort ———————————————————————————————
void heapify(std::vector<long long>& a, size_t n, size_t i) {
    size_t largest = i, l = 2*i+1, r = 2*i+2;
    if (l < n && a[l] > a[largest]) largest = l;
    if (r < n && a[r] > a[largest]) largest = r;
    if (largest != i) {
        std::swap(a[i], a[largest]);
        heapify(a, n, largest);
    }
}
void heap_sort(std::vector<long long>& a) {
    size_t n = a.size();
    for (size_t i = n/2; i-- > 0; )
        heapify(a, n, i);
    for (size_t i = n; i-- > 1; ) {
        std::swap(a[0], a[i]);
        heapify(a, i, 0);
    }
}

// ——— Quick sort (random pivot) ————————————————————
static std::mt19937_64 RNG{ std::random_device{}() };
int partition_rand(std::vector<long long>& a, int low, int high) {
    std::uniform_int_distribution<int> dist(low, high);
    std::swap(a[dist(RNG)], a[high]);
    long long pivot = a[high];
    int i = low - 1;
    for (int j = low; j < high; ++j) {
        if (a[j] < pivot) std::swap(a[++i], a[j]);
    }
    std::swap(a[i+1], a[high]);
    return i+1;
}
void quick_sort(std::vector<long long>& a, int low, int high) {
    if (low < high) {
        int p = partition_rand(a, low, high);
        quick_sort(a, low, p-1);
        quick_sort(a, p+1, high);
    }
}

// ——— Merge sort ——————————————————————————————
void merge(std::vector<long long>& a, int l, int m, int r) {
    int n1 = m-l+1, n2 = r-m;
    std::vector<long long> L(n1), R(n2);
    for (int i = 0; i < n1; ++i) L[i] = a[l+i];
    for (int j = 0; j < n2; ++j) R[j] = a[m+1+j];
    int i=0, j=0, k=l;
    while (i<n1 && j<n2)
        a[k++] = (L[i] <= R[j] ? L[i++] : R[j++]);
    while (i<n1) a[k++] = L[i++];
    while (j<n2) a[k++] = R[j++];
}
void merge_sort(std::vector<long long>& a, int l, int r) {
    if (l >= r) return;
    int m = l + (r-l)/2;
    merge_sort(a, l, m);
    merge_sort(a, m+1, r);
    merge(a, l, m, r);
}
void merge_sort(std::vector<long long>& a) {
    if (!a.empty())
        merge_sort(a, 0, int(a.size())-1);
}

// ——— Bubble, Insertion, Selection, Shell —————————
void bubble_sort(std::vector<long long>& a) {
    for (size_t i=0, n=a.size(); i+1<n; ++i) {
        bool sw=false;
        for (size_t j=0; j+1<n-i; ++j)
            if (a[j]>a[j+1]){ std::swap(a[j],a[j+1]); sw=true; }
        if (!sw) break;
    }
}
void insertion_sort(std::vector<long long>& a) {
    for (size_t i=1, n=a.size(); i<n; ++i) {
        long long key = a[i];
        int j = int(i)-1;
        while (j>=0 && a[j]>key) {
            a[j+1] = a[j--];
        }
        a[j+1] = key;
    }
}
void selection_sort(std::vector<long long>& a) {
    for (size_t i=0, n=a.size(); i+1<n; ++i) {
        size_t m=i;
        for (size_t j=i+1; j<n; ++j)
            if (a[j]<a[m]) m=j;
        if (m!=i) std::swap(a[i], a[m]);
    }
}
void shell_sort(std::vector<long long>& a) {
    for (size_t gap=a.size()/2; gap>0; gap/=2) {
        for (size_t i=gap; i<a.size(); ++i) {
            long long tmp = a[i];
            size_t j = i;
            while (j>=gap && a[j-gap]>tmp) {
                a[j] = a[j-gap];
                j -= gap;
            }
            a[j] = tmp;
        }
    }
}

// ——— List all .txt files in a folder ————————————
std::vector<std::string> list_txt_files(const std::string& folder) {
    std::vector<std::string> out;
    WIN32_FIND_DATAA fd;
    std::string base = folder;
    if (!base.empty() && (base.back()=='\\'||base.back()=='/'))
        base.pop_back();
    std::string pattern = base + "\\*.txt";

    HANDLE h = FindFirstFileA(pattern.c_str(), &fd);
    if (h == INVALID_HANDLE_VALUE) return out;
    do {
        if (!(fd.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY))
            out.push_back(base + "\\" + fd.cFileName);
    } while (FindNextFileA(h, &fd));
    FindClose(h);
    return out;
}

int main(int argc, char* argv[]) {
    if (argc != 3) {
        std::cerr << "Usage: " << argv[0]
                  << " <folder_path> <timings.csv>\n";
        return 1;
    }
    std::string folder = argv[1], csv = argv[2];

    // Prepare CSV file
    bool need_header = false;
    {
        std::ifstream in(csv);
        if (!in.good() || in.peek() == std::ifstream::traits_type::eof())
            need_header = true;
    }
    std::ofstream out(csv, std::ios::app);
    if (!out) {
        std::cerr << "Error opening CSV: " << csv << "\n";
        return 1;
    }
    if (need_header)
        out << "algorithm,filename,time_milliseconds\n";

    // Gather files
    auto files = list_txt_files(folder);
    if (files.empty()) {
        std::cerr << "No .txt files found in \"" << folder << "\"\n";
        return 1;
    }

    // Build algorithm list with wrappers
    using SortFn = void(*)(std::vector<long long>&);
    auto quick_wrap = [](std::vector<long long>& v){
        quick_sort(v, 0, int(v.size())-1);
    };
    auto merge_wrap = [](std::vector<long long>& v){
        merge_sort(v);
    };

    std::vector<std::pair<std::string,SortFn>> algos = {
        {"bubble",    bubble_sort},
        {"insertion", insertion_sort},
        {"selection", selection_sort},
        {"shell",     shell_sort},
        {"heap",      heap_sort},
        {"radix",     radix_sort},
        {"quick",     quick_wrap},
        {"merge",     merge_wrap}
    };

    // Process each file with each algorithm
    for (auto& f : files) {
        // read original data
        std::vector<long long> orig;
        {
            std::ifstream fin(f);
            long long x;
            while (fin >> x) orig.push_back(x);
        }
        for (auto& algo : algos) {
            const std::string& name = algo.first;
            SortFn fn               = algo.second;

            auto data = orig;  // make a fresh copy
            auto t0   = std::chrono::high_resolution_clock::now();
            fn(data);
            auto t1   = std::chrono::high_resolution_clock::now();
            auto ms   = std::chrono::duration_cast<
                         std::chrono::milliseconds>(t1 - t0).count();

            out << name << "," << '"' << f << '"' << "," << ms << "\n";
            std::cout << "[" << name << "] " << f
                      << ": " << ms << " ms\n";
        }
    }

    std::cout << "Done. Processed " << files.size() << " files.\n";
    return 0;
}
