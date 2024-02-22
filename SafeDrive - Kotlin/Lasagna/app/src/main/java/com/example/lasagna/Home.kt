package com.example.lasagna

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import androidx.fragment.app.Fragment
import com.example.lasagna.databinding.ActivityHomeBinding
import com.google.android.material.navigation.NavigationBarView

class Home : AppCompatActivity() {

    private lateinit var binding : ActivityHomeBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityHomeBinding.inflate(layoutInflater)
        setContentView(binding.root)

        val scannerFragment = ScannerFragment()
        val mapFragment = MapFragment()
        val dashboardFragment = DashboardFragment()

        setCurrentFragment(mapFragment)

        binding.bottomNavigationView.setOnItemSelectedListener {
            when (it.itemId) {
                R.id.micamera -> setCurrentFragment(scannerFragment)
                R.id.mimap -> setCurrentFragment(mapFragment)
                R.id.midashboard -> setCurrentFragment(dashboardFragment)
            }
            true
        }
    }

    private fun setCurrentFragment(fragment: Fragment) =
        supportFragmentManager.beginTransaction().apply {
            replace(R.id.flFragment, fragment)
            commit()
        }
}