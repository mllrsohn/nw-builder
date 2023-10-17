// Copyright 2019 the V8 project authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#ifndef V8_CODEGEN_PENDING_OPTIMIZATION_TABLE_H_
#define V8_CODEGEN_PENDING_OPTIMIZATION_TABLE_H_

#include "src/common/globals.h"

namespace v8 {
namespace internal {

class IsCompiledScope;

// This class adds the functionality to properly test the optimized code. This
// is only for use in tests. All these functions should only be called when
// testing_d8_flag_for_tests is set.
class ManualOptimizationTable {
 public:
  // This function should be called before we mark the function for
  // optimization. It should be called when |function| is already compiled and
  // has a feedback vector allocated, and it blocks heuristic optimization.
  //
  // This also holds on to the bytecode strongly, preventing the bytecode from
  // being flushed.
  static void MarkFunctionForManualOptimization(
      Isolate* isolate, Handle<JSFunction> function,
      IsCompiledScope* is_compiled_scope);

  // This function should be called when the function is marked for optimization
  // via the intrinsics. This will check whether
  // MarkFunctionForManualOptimization was called with this function.
  static void CheckMarkedForManualOptimization(Isolate* isolate,
                                               JSFunction function);

  // Returns true if MarkFunctionForManualOptimization was called with this
  // function.
  static bool IsMarkedForManualOptimization(Isolate* isolate,
                                            JSFunction function);
};

}  // namespace internal
}  // namespace v8

#endif  // V8_CODEGEN_PENDING_OPTIMIZATION_TABLE_H_
