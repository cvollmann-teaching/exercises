// uncomment to disable assert()
// #define NDEBUG
#include <cassert>
#include <map>
#include <list>
#include <vector>
#include <iostream>
// Use (void) to silence unused warnings.
#define assertm(exp, msg) assert(((void)msg, exp))
typedef std::map<int, double> sparsevector;
struct  sparsevectorpair {
    sparsevector vec1;
    sparsevector vec2;
};
struct  vectorpair {
    std::vector<double> vec1;
    std::vector<double> vec2;
};

bool contains(const sparsevector vec, const int index){
    return vec.find(index) != vec.end();
}

double dot(const std::map<int, double> &sparsevec1, const std::map<int, double> &sparsevec2){
    double sum = 0.0;
    for(const auto& pair : sparsevec1){
        const int index = pair.first;
        const double value1 = pair.second;
        if (contains(sparsevec2, index))
        {
            sum += sparsevec2.at(index) * value1;
        }
    }
    return sum;
}

double dot(const std::vector<double> &vec1, const std::vector<double> &vec2){
    assertm(vec1.size() == vec2.size(), "Vector sizes must be equal.");
    double sum = 0.0;
    for(int k=0; k<vec1.size(); k++){
        sum += vec1[k]*vec2[k];
    }
    return sum;
}

double test_dot_sparse(){
    std::list<sparsevectorpair> input {
            {
                {
                        {0, 1.0},
                        {1, 2.0},
                        {2, 3.0}
                },
                {
                        {0, 1.0},
                        {1, 2.0},
                        {2, 3.0}
                },
            },
            {
                {
                         {0, 1.0},
                         {1, 2.0},
                         {2, 3.0}
                 },
                 {
                         {3, 1.0},
                         {4, 2.0},
                         {5, 3.0}
                 },
            },
            {
            {
                    {}
                },
                {
                        {3, 1.0},
                        {4, 2.0},
                        {5, 3.0}
                },
            }
    };
    std::list<double> expected {
        14.0, 0.0, 0.0
    };
    while (!input.empty()){
        const auto vecpair = input.front();
        const auto expectedscalar = expected.front();
        const auto result = dot(vecpair.vec1, vecpair.vec2);
        assertm(result == expectedscalar, "dot not equal scalar");
        input.pop_front();
        expected.pop_front();
    }
    return 0;

}

double test_dot_dense(){
    std::list<vectorpair> input {
                    {
                            {1.0, 2.0, 3.0},
                            {1.0, 2.0, 3.0}
                    },
                    {
                            {1.0, 2.0, 3.0},
                            {0.0, 0.0, 0.0}
                    }
    };
    std::list<double> expected {
            14.0, 0.0
    };
    while (!input.empty()){
        const auto vecpair = input.front();
        const auto expectedscalar = expected.front();
        const auto result = dot(vecpair.vec1, vecpair.vec2);
        assertm(result == expectedscalar, "dot not equal scalar");
        input.pop_front();
        expected.pop_front();
    }
    return 0;
}

int main(){
    test_dot_sparse();
    test_dot_dense();
}