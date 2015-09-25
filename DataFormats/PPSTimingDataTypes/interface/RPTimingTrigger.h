#ifndef DataFormats_PPSTimingDataTypes_Timing_TRIGGER_H
#define DataFormats_PPSTimingDataTypes_Timing_TRIGGER_H

#include "DataFormats/PPSTimingDataTypes/interface/PPSTimingTypes.h"

class RPTimingTrigger {
 public:
  RPTimingTrigger(TimingId det_id=0, unsigned short sector_no=0)
    {det_id_=det_id; sector_no_=sector_no;};
  inline TimingId GetDetId() const {return det_id_;}
  inline unsigned short GetSector() const {return sector_no_;}
  
 private:
  TimingId det_id_;
  unsigned short sector_no_;
};

// Comparison operators
inline bool operator<( const RPTimingTrigger& one, const RPTimingTrigger& other) {
  if(one.GetDetId() < other.GetDetId())
    return true;
  else if(one.GetDetId() == other.GetDetId())
    return one.GetSector() < other.GetSector();
  else 
    return false;
}

#endif
