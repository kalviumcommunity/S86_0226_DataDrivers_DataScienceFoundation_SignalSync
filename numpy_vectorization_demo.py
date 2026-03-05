#!/usr/bin/env python3
"""
SignalSync NumPy Vectorization Milestone
A comprehensive demonstration of vectorized operations vs Python loops
for efficient numerical computing in traffic analysis
"""

import numpy as np
import time


def demonstrate_loop_vs_vectorized():
    """1. Understanding Loop-Based vs Vectorized Code"""
    print("=" * 60)
    print("🔄 1. LOOP-BASED vs VECTORIZED CODE COMPARISON")
    print("=" * 60)
    
    # Sample traffic data - hourly vehicle counts for a week
    traffic_volumes = np.array([850, 1200, 900, 1400, 1800, 1600, 1100, 
                               750, 1100, 850, 1300, 1750, 1550, 1050,
                               820, 1250, 920, 1450, 1820, 1620, 1120])
    
    print("Traffic volume data (vehicles per hour):")
    print(f"Array shape: {traffic_volumes.shape}")
    print(f"Sample data: {traffic_volumes[:7]}...")
    print()
    
    print("❌ LOOP-BASED APPROACH:")
    print("```python")
    print("# BAD: Using Python loop to calculate speed penalties")
    print("speed_penalties = []")
    print("for volume in traffic_volumes:")
    print("    if volume > 1000:")
    print("        penalty = volume * 0.1  # 10% speed reduction")
    print("    else:")
    print("        penalty = 0")
    print("    speed_penalties.append(penalty)")
    print("```")
    
    # Demonstrate the loop approach
    speed_penalties_loop = []
    start_time = time.time()
    for volume in traffic_volumes:
        if volume > 1000:
            penalty = volume * 0.1  # 10% speed reduction for high traffic
        else:
            penalty = 0
        speed_penalties_loop.append(penalty)
    loop_time = time.time() - start_time
    
    print(f"Loop result (first 5): {speed_penalties_loop[:5]}")
    print(f"Loop execution time: {loop_time:.6f} seconds")
    print()
    
    print("✅ VECTORIZED APPROACH:")
    print("```python")
    print("# GOOD: Using NumPy vectorized operations")
    print("speed_penalties = np.where(traffic_volumes > 1000, ")
    print("                          traffic_volumes * 0.1, 0)")
    print("```")
    
    # Demonstrate the vectorized approach
    start_time = time.time()
    speed_penalties_vectorized = np.where(traffic_volumes > 1000, 
                                        traffic_volumes * 0.1, 0)
    vectorized_time = time.time() - start_time
    
    print(f"Vectorized result (first 5): {speed_penalties_vectorized[:5]}")
    print(f"Vectorized execution time: {vectorized_time:.6f} seconds")
    print()
    
    # Verify results are identical
    results_match = np.allclose(speed_penalties_loop, speed_penalties_vectorized)
    print(f"Results identical: {results_match}")
    
    if len(traffic_volumes) > 10:
        speedup = loop_time / vectorized_time if vectorized_time > 0 else float('inf')
        print(f"Performance improvement: {speedup:.1f}x faster")
    
    print()
    print("🎯 Key differences:")
    print("  • Loop: 7 lines of code, explicit iteration")
    print("  • Vectorized: 1 line of code, operates on entire array")
    print("  • Vectorized code is more readable and maintainable")
    print("  • NumPy handles the iteration internally (optimized C code)")
    print()
    print("✓ Loop vs vectorized comparison demonstrated")


def demonstrate_vectorized_arithmetic():
    """2. Applying Vectorized Arithmetic Operations"""
    print("=" * 60)
    print("🧮 2. VECTORIZED ARITHMETIC OPERATIONS")
    print("=" * 60)
    
    # Traffic data arrays
    morning_traffic = np.array([420, 850, 1200, 980, 750])
    evening_traffic = np.array([380, 920, 1350, 1100, 680])
    road_capacities = np.array([2000, 1800, 1500, 1600, 1400])
    
    print("Traffic analysis data:")
    print(f"Morning volumes: {morning_traffic}")
    print(f"Evening volumes: {evening_traffic}")
    print(f"Road capacities: {road_capacities}")
    print()
    
    print("🧮 Arithmetic operations on entire arrays:")
    
    # Total daily traffic (vectorized addition)
    total_daily_traffic = morning_traffic + evening_traffic
    print(f"Total daily traffic: {total_daily_traffic}")
    print("  → morning_traffic + evening_traffic")
    
    # Average traffic (vectorized division)
    average_traffic = total_daily_traffic / 2
    print(f"Average traffic: {average_traffic}")
    print("  → total_daily_traffic / 2")
    
    # Traffic utilization percentage (vectorized operations)
    utilization_percentage = (total_daily_traffic / road_capacities) * 100
    print(f"Road utilization: {utilization_percentage.round(1)}%")
    print("  → (total_daily_traffic / road_capacities) * 100")
    
    # Congestion factor calculation
    congestion_factor = np.sqrt(total_daily_traffic / 1000)
    print(f"Congestion factor: {congestion_factor.round(2)}")
    print("  → np.sqrt(total_daily_traffic / 1000)")
    
    # Peak hour multiplier
    peak_multiplier = 1.5
    peak_estimated_traffic = average_traffic * peak_multiplier
    print(f"Peak estimates: {peak_estimated_traffic.round(0)}")
    print(f"  → average_traffic * {peak_multiplier}")
    
    print()
    print("🧮 Mathematical functions work element-wise:")
    
    # Logarithmic scale for very high traffic
    log_scaled_traffic = np.log10(total_daily_traffic)
    print(f"Log-scaled traffic: {log_scaled_traffic.round(2)}")
    print("  → np.log10(total_daily_traffic)")
    
    # Exponential growth model
    growth_rates = np.array([1.02, 1.05, 1.03, 1.04, 1.01])  # 2-5% annual growth
    projected_traffic = total_daily_traffic * np.power(growth_rates, 5)  # 5 years
    print(f"5-year projections: {projected_traffic.round(0)}")
    print("  → total_daily_traffic * np.power(growth_rates, 5)")
    
    print()
    print("✅ Benefits of vectorized arithmetic:")
    print("  • No explicit loops needed")
    print("  • Operations apply to all elements automatically")
    print("  • Code mirrors mathematical notation")
    print("  • Faster execution than Python loops")
    print("  • Broadcasting allows operations with different shapes")
    print()
    print("✓ Vectorized arithmetic operations demonstrated")


def demonstrate_vectorized_comparisons():
    """3. Using Vectorized Comparisons and Conditions"""
    print("=" * 60)
    print("🔍 3. VECTORIZED COMPARISONS AND CONDITIONS")
    print("=" * 60)
    
    # Traffic monitoring data
    current_volumes = np.array([450, 1200, 800, 1500, 300, 1800, 650, 1100])
    speed_limits = np.array([35, 55, 45, 65, 25, 55, 40, 50])
    weather_visibility = np.array([10, 8, 5, 9, 3, 6, 7, 4])  # miles
    
    print("Traffic monitoring arrays:")
    print(f"Traffic volumes: {current_volumes}")
    print(f"Speed limits: {speed_limits} mph")
    print(f"Visibility: {weather_visibility} miles")
    print()
    
    print("🔍 Boolean array comparisons:")
    
    # High traffic conditions (vectorized comparison)
    high_traffic_mask = current_volumes > 1000
    print(f"High traffic (>1000): {high_traffic_mask}")
    print("  → current_volumes > 1000")
    
    # Low visibility conditions
    low_visibility_mask = weather_visibility < 5
    print(f"Low visibility (<5mi): {low_visibility_mask}")
    print("  → weather_visibility < 5")
    
    # High speed roads
    high_speed_mask = speed_limits >= 55
    print(f"High speed (≥55mph): {high_speed_mask}")
    print("  → speed_limits >= 55")
    
    print()
    print("🔍 Logical operations on boolean arrays:")
    
    # Dangerous conditions: high traffic AND low visibility
    dangerous_conditions = high_traffic_mask & low_visibility_mask
    print(f"Dangerous (high traffic AND low visibility): {dangerous_conditions}")
    print("  → high_traffic_mask & low_visibility_mask")
    
    # Alert conditions: high traffic OR low visibility
    alert_conditions = high_traffic_mask | low_visibility_mask
    print(f"Alert needed (high traffic OR low visibility): {alert_conditions}")
    print("  → high_traffic_mask | low_visibility_mask")
    
    # Highway concerns: high speed AND (high traffic OR low visibility)
    highway_concerns = high_speed_mask & (high_traffic_mask | low_visibility_mask)
    print(f"Highway concerns: {highway_concerns}")
    print("  → high_speed_mask & (high_traffic_mask | low_visibility_mask)")
    
    print()
    print("🔍 Extracting data based on conditions:")
    
    # Get volumes where traffic is high
    high_traffic_volumes = current_volumes[high_traffic_mask]
    print(f"High traffic volumes: {high_traffic_volumes}")
    print("  → current_volumes[high_traffic_mask]")
    
    # Count conditions
    num_high_traffic = np.sum(high_traffic_mask)
    num_dangerous = np.sum(dangerous_conditions)
    print(f"Count high traffic locations: {num_high_traffic}")
    print(f"Count dangerous locations: {num_dangerous}")
    print("  → np.sum(boolean_array)")
    
    # Any/All conditions
    any_dangerous = np.any(dangerous_conditions)
    all_highways = np.all(speed_limits >= 25)
    print(f"Any dangerous conditions: {any_dangerous}")
    print(f"All roads ≥25mph: {all_highways}")
    print("  → np.any(), np.all()")
    
    print()
    print("🔍 Conditional value assignment:")
    
    # Assign speed recommendations based on conditions
    # Low traffic: maintain speed, high traffic: reduce by 10mph
    recommended_speeds = np.where(current_volumes > 1000, 
                                speed_limits - 10, 
                                speed_limits)
    print(f"Recommended speeds: {recommended_speeds}")
    print("  → np.where(condition, value_if_true, value_if_false)")
    
    # Multi-condition assignment using np.select
    conditions = [weather_visibility < 3, 
                 current_volumes > 1500,
                 (current_volumes > 1000) & (weather_visibility < 5)]
    choices = ["SEVERE WEATHER ALERT",
              "HEAVY TRAFFIC ALERT", 
              "CAUTION ADVISED"]
    alerts = np.select(conditions, choices, default="NORMAL CONDITIONS")
    
    print()
    print("Alert system based on multiple conditions:")
    for i, alert in enumerate(alerts):
        print(f"  Location {i+1}: {alert}")
    
    print()
    print("✅ Benefits of vectorized conditions:")
    print("  • No loops needed for element-wise comparisons")
    print("  • Boolean arrays enable powerful filtering")
    print("  • Logical operators work element-wise")
    print("  • Conditional assignment in single operations")
    print("  • Easy counting and aggregation of conditions")
    print()
    print("✓ Vectorized comparisons and conditions demonstrated")


def demonstrate_vectorization_mistakes():
    """4. Avoiding Common Vectorization Mistakes"""
    print("=" * 60)
    print("⚠️  4. COMMON VECTORIZATION MISTAKES TO AVOID")
    print("=" * 60)
    
    print("❌ MISTAKE 1: Incompatible array shapes")
    
    traffic_data = np.array([100, 200, 300, 400])
    multipliers = np.array([1.1, 1.2])  # Different size!
    
    print(f"Traffic data shape: {traffic_data.shape}")
    print(f"Multipliers shape: {multipliers.shape}")
    
    try:
        # This will fail due to incompatible shapes
        result = traffic_data * multipliers
    except ValueError as e:
        print(f"❌ Error: {e}")
    
    print("\n✅ FIX: Ensure compatible shapes or use broadcasting")
    # Reshape multipliers to be compatible
    multipliers_reshaped = np.array([1.1, 1.2, 1.1, 1.2])  # Same length
    result = traffic_data * multipliers_reshaped
    print(f"Fixed result: {result}")
    
    print()
    print("❌ MISTAKE 2: Unnecessary loops for simple operations")
    
    volumes = np.array([850, 1200, 600, 1400, 300])
    
    print("Bad approach (unnecessary loop):")
    print("```python")
    print("adjusted_volumes = []")
    print("for vol in volumes:")
    print("    adjusted_volumes.append(vol * 1.15)")
    print("```")
    
    print("Good approach (vectorized):")
    print("```python")
    print("adjusted_volumes = volumes * 1.15")
    print("```")
    
    # Show both results
    bad_result = []
    for vol in volumes:
        bad_result.append(vol * 1.15)
    good_result = volumes * 1.15
    
    print(f"Both give same result: {np.allclose(bad_result, good_result)}")
    print(f"Vectorized result: {good_result}")
    
    print()
    print("❌ MISTAKE 3: Overusing np.where for simple conditions")
    
    print("Unnecessarily complex:")
    print("```python")
    print("# Overly complex for simple threshold")
    print("result = np.where(volumes > 1000, 1, 0)")
    print("```")
    
    print("Simpler and clearer:")
    print("```python")
    print("# Direct comparison is clearer")
    print("result = volumes > 1000")
    print("```")
    
    complex_result = np.where(volumes > 1000, 1, 0)
    simple_result = volumes > 1000
    print(f"Complex result: {complex_result}")
    print(f"Simple result: {simple_result}")
    print("Use simple boolean arrays when you don't need specific values.")
    
    print()
    print("❌ MISTAKE 4: Premature optimization")
    
    print("Don't sacrifice readability for minor performance gains:")
    print()
    print("Readable (preferred):")
    print("```python")
    print("congestion_ratio = traffic_volume / road_capacity")
    print("is_congested = congestion_ratio > 0.8")
    print("```")
    
    print("Over-optimized (harder to read):")
    print("```python")
    print("is_congested = (traffic_volume / road_capacity) > 0.8")
    print("```")
    
    # Both approaches
    traffic_volume = np.array([800, 1600, 1200])
    road_capacity = np.array([1000, 2000, 1500])
    
    # Readable approach
    congestion_ratio = traffic_volume / road_capacity
    is_congested_readable = congestion_ratio > 0.8
    
    # Compact approach
    is_congested_compact = (traffic_volume / road_capacity) > 0.8
    
    print(f"Both approaches identical: {np.array_equal(is_congested_readable, is_congested_compact)}")
    print("Choose readability unless performance is critical.")
    
    print()
    print("✅ Best practices for vectorization:")
    print("  • Check array shapes before operations")
    print("  • Use vectorized operations instead of loops")
    print("  • Keep operations simple and readable")
    print("  • Don't optimize prematurely")
    print("  • Use descriptive variable names")
    print("  • Test with small arrays first")
    print()
    print("✓ Common vectorization mistakes and solutions demonstrated")


def demonstrate_performance_comparison():
    """5. Performance and Readability Benefits"""
    print("=" * 60)
    print("🚀 5. PERFORMANCE AND READABILITY BENEFITS")
    print("=" * 60)
    
    # Create larger dataset for performance testing
    large_traffic_data = np.random.randint(100, 2000, size=100000)
    print(f"Large dataset size: {large_traffic_data.shape[0]:,} traffic readings")
    print()
    
    print("🚀 Performance comparison:")
    
    # Loop-based approach
    print("Testing loop-based calculation...")
    start_time = time.time()
    
    congestion_scores_loop = []
    for volume in large_traffic_data:
        if volume > 1500:
            score = volume * 0.8 + 200  # Heavy congestion penalty
        elif volume > 1000:
            score = volume * 0.6 + 100  # Moderate congestion penalty  
        else:
            score = volume * 0.4        # Light traffic
        congestion_scores_loop.append(score)
    
    loop_time = time.time() - start_time
    print(f"Loop approach time: {loop_time:.4f} seconds")
    
    # Vectorized approach
    print("Testing vectorized calculation...")
    start_time = time.time()
    
    congestion_scores_vectorized = np.where(
        large_traffic_data > 1500,
        large_traffic_data * 0.8 + 200,  # Heavy congestion
        np.where(
            large_traffic_data > 1000,
            large_traffic_data * 0.6 + 100,  # Moderate congestion
            large_traffic_data * 0.4         # Light traffic
        )
    )
    
    vectorized_time = time.time() - start_time
    print(f"Vectorized approach time: {vectorized_time:.4f} seconds")
    
    # Calculate speedup
    speedup = loop_time / vectorized_time if vectorized_time > 0 else float('inf')
    print(f"Performance improvement: {speedup:.1f}x faster")
    
    # Verify results are identical
    results_match = np.allclose(congestion_scores_loop, congestion_scores_vectorized)
    print(f"Results identical: {results_match}")
    
    print()
    print("📚 Readability comparison:")
    
    print("Loop-based code:")
    print("```python")
    print("congestion_scores = []")
    print("for volume in traffic_data:")
    print("    if volume > 1500:")
    print("        score = volume * 0.8 + 200")
    print("    elif volume > 1000:")
    print("        score = volume * 0.6 + 100")  
    print("    else:")
    print("        score = volume * 0.4")
    print("    congestion_scores.append(score)")
    print("```")
    print(f"Lines of code: 8")
    
    print("\nVectorized code:")
    print("```python")
    print("congestion_scores = np.where(")
    print("    traffic_data > 1500,")
    print("    traffic_data * 0.8 + 200,")
    print("    np.where(")
    print("        traffic_data > 1000,")
    print("        traffic_data * 0.6 + 100,")
    print("        traffic_data * 0.4")
    print("    )")
    print(")")
    print("```")
    print(f"Lines of code: 9 (but more concise logic)")
    
    print()
    print("🚀 Key benefits of vectorization:")
    print(f"  • Performance: {speedup:.1f}x faster execution")
    print("  • Conciseness: Operations on entire arrays")
    print("  • Readability: Mathematical notation style")
    print("  • Maintainability: Less error-prone than loops")
    print("  • Scalability: Handles large datasets efficiently")
    print("  • NumPy integration: Works with all NumPy functions")
    
    print()
    print("🎯 When to use vectorization:")
    print("  ✓ Mathematical operations on arrays")
    print("  ✓ Element-wise transformations")
    print("  ✓ Conditional value assignments")
    print("  ✓ Aggregations and reductions")
    print("  ✓ Boolean masking and filtering")
    
    print()
    print("⚠️  When loops might be necessary:")
    print("  • Complex logic that depends on previous elements")
    print("  • Operations that can't be expressed element-wise")
    print("  • Interactive processes requiring user input")
    print("  • File I/O or external API calls in the loop")
    
    print()
    print("✓ Performance and readability benefits demonstrated")


def main():
    """Main function demonstrating all NumPy vectorization concepts"""
    print("🔢" * 20)
    print("SIGNALSYNC NUMPY VECTORIZATION MILESTONE")
    print("Replacing Python Loops with Efficient Array Operations")
    print("🔢" * 20)
    print()
    
    # Execute all demonstrations in sequence
    demonstrate_loop_vs_vectorized()
    print("\n")
    
    demonstrate_vectorized_arithmetic()
    print("\n")
    
    demonstrate_vectorized_comparisons()
    print("\n")
    
    demonstrate_vectorization_mistakes()
    print("\n")
    
    demonstrate_performance_comparison()
    print("\n")
    
    # Final summary
    print("=" * 60)
    print("✅ NUMPY VECTORIZATION MILESTONE COMPLETE")
    print("=" * 60)
    print()
    print("📚 Skills Demonstrated:")
    print("   ✓ Loop-based vs vectorized code comparison")
    print("   ✓ Vectorized arithmetic operations on arrays")
    print("   ✓ Vectorized comparisons and boolean logic")
    print("   ✓ Common vectorization mistakes and solutions")
    print("   ✓ Performance and readability benefits")
    print()
    print("🎯 Key Learning Outcomes:")
    print("   • Vectorized operations replace explicit loops")
    print("   • NumPy functions work element-wise on arrays")
    print("   • Boolean arrays enable powerful filtering")
    print("   • Vectorization improves both speed and readability")
    print("   • Think in terms of array operations, not iterations")
    print()
    print("💡 Vectorization Principles:")
    print("   • Tell NumPy WHAT to do, not HOW to iterate")
    print("   • Operations apply to entire arrays automatically")
    print("   • Use comparison operators to create boolean masks")
    print("   • Combine conditions with &, |, and ~ operators")
    print("   • Prefer np.where() for conditional value assignment")
    print()
    print("🚀 Ready for advanced NumPy operations and data analysis!")
    print("🔢" * 20)


if __name__ == "__main__":
    main()